
import pymysql
import random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={}#创建一个空的字典
#开户逻辑
bank_name="狼腾测试猿银行"
money = 0
con = pymysql.connect(host="localhost", user="root", password="123456", database="bank")
cursor = con.cursor()
#                第一个对应第一个 不是名称对应名称
# def bank_adduser(account,username,password,country,province,street,door):
#     if  len(bank) >100:
#         return 3
#     if username in bank:#  如变量在容器内执行下面的代码
#         return 2
#     bank[username]={
#         "account":account,#
#         "password":password,
#         "country":country,
#         "province":province,
#         "street":street,
#         "door":door,
#         "money":0,
#         "bank_name":bank_name
#     }
#     return 1

# 添加用户
def adduser():#定义了一个方法
    sql = "select count(*)  from gsbank"
    cursor.execute(sql)
    data = cursor.fetchall()
    if len(data) >= 100:
        print("你去别的银行吧")
    account = random.randint(10000000, 99999999)
    sql1 = "select * from gsbank where account = %s"
    param = [account]
    cursor.execute(sql1, param)
    data = cursor.fetchall()
    if len(data) != 0:
            print("开户失败，你别重复")
    else:
            username = str(input("请输入您的用户名："))
            while True:
                passwor = str(input("请输入您的密码："))
                if len(passwor) < 6:
                    print("您设置的密码不足6位，请再次输入！")
                else:
                    print("请输入您的地址：")
                    break
            country = str(input("\t\t请输入您的国家："))
            province = str(input("\t\t请输入您的省份："))
            street = str(input("\t\t请输入您的街道："))
            door = input("\t\t请输入您的门牌号：")

            sql2 = "insert into gsbank values(%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
            param = [account,username,passwor,country,province,street,door,money,bank_name]
            cursor.execute(sql2, param)
            con.commit()
            info = '''
                        ------------个人信息------------
                        用户名:%s
                        账号：%s
                        密码：*****
                        国籍：%s
                        省份：%s
                        街道：%s
                        门牌号：%s
                        余额：%s
                        开户行名称：%s
                    '''
            # 每个元素都可传入%
            print(info % (username, account, country, province, street, door, money, bank_name))
            # cursor.close()
            # con.close()


#     stast=bank_adduser(account,username,password,country,province,street,door)
#     #        调用方法   （元素，，，，，，，，，）
#     if stast ==3 :
#         print("你去别的银行吧")
#     elif stast== 2:
#         print("开户失败，你别重复")
#     elif stast== 1:
#         info = '''
#                     ------------个人信息------------
#                     用户名:%s
#                     账号：%s
#                     密码：*****
#                     国籍：%s
#                     省份：%s
#                     街道：%s
#                     门牌号：%s
#                     余额：%s
#                     开户行名称：%s
#                 '''
#         # 每个元素都可传入%
#         print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
# #{'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 0, 'bank_name': '狼腾测试猿银行'}}


# 存钱
def addmoney():
    acc1 = int(input("请输入您的账号："))
    sql3 = "select * from gsbank where account = %s"
    param = [acc1]
    cursor.execute(sql3,param)
    data = cursor.fetchall()
    if len(data) == 1:
        money1 = float(input("请输入您需要存入的金额："))
        money2 = data[0][7] + money1
        sql4 = "update  gsbank  set money = %s + money where account = %s"
        param2 = [money2,acc1]
        cursor.execute(sql4,param2)
        con.commit()
        info = '''
                                ------------个人信息------------
                    用户名:%s
                    账号：%s
                    余额：%s
                    开户行名称：%s
             '''
        print(info % (data[0][1], data[0][0] , money2 , data[0][0]))
    else:
        print("您的账户输入错误！")


    # username = input("请输入您的用户名：")
    # account = int(input("请输入您的账号："))
    # # account ="account" in bank
    # if account == bank[username]["account"]:
    #     money = bank[username]['money']
    #     money1 = int(input("请输入您需要存入的金额："))
    #     money = money + money1
    #     bank[username]['money'] = money
    #     print("您现在的余额为：",money)
    # else:
    #     print("您的账号输入错误!")

# 取钱
# def getmoney():
#     username = input("请输入您的用户名：")
#     account = int(input("请输入您的账号："))
#     if account != bank[username]["account"]:
#         print("您的账户输入错误!")
#     else:
#         password = str(input("请输入您的密码："))
#         if password != bank[username]["password"]:
#             print("您的密码输入错误！")
#         else:
#             money = bank[username]["money"]
#             money1 = int(input("请输入您需要取出的余额："))
#             if money1 < bank[username]["money"]:
#                 money = bank[username]["money"] - money1
#                 bank[username]["money"] = money
#                 print("取出",money1 ,"元后，您的余额为：",money,"元")
#             else:
#                 print("您的余额不足无法取出！")



# 转账
# def movemoney():
#     username1 = input("请输入转出用户名：")
#     username2 = input("请输入转入用户名：")
#     account1 = int(input("请输入转出的账号："))
#     account2 = int(input("请输入转入的账号："))
#     if account1 != bank[username1]["account"] and account2 != bank[username2]["account"]:
#         print("账号错误")
#     else:
#         password1 = str(input("请输入转出账号的密码："))
#         password2 = str(input("请输入转入账号的密码："))
#         #password = bank[username]["password"]
#         if password1 != bank[username1]["password"] and password2 != bank[username2]["password"]:
#             print("密码错误")
#         else:
#             #money = bank[username]["money"]
#             mvmoney = int(input("请输入您要转出的金额："))
#             if mvmoney < bank[username1]["money"]:
#                 money = bank[username1]["money"] - mvmoney
#                 bank[username1]["money"] = money
#                 getmoney = bank[username2]["money"] + mvmoney
#                 bank[username2]["money"] = getmoney
#                 print("转出",mvmoney,"元后，您的账号",account1,"余额为：",money)
#                 print("转入账号现在的余额为：",getmoney)
#             else:
#                 print("您的余额不足")
#




while True:
    begin = input("请选择业务：")
    if begin =="1": #您输入的业务等于1执行开户操作
        adduser()
    elif begin == "2":
        print(2,"、存钱")
        addmoney()
    elif begin == "3":
        print(3,"、取钱")
        # getmoney()
    elif begin == "4":
        print(4,"、转账")
        # movemoney()
    elif begin == "5":
        print(5,"、查询")
    else:
        print(6,"、退出")
        break