# 1、抽奖
import random
import sys
print("欢迎来到XX商城！请先抽奖！")
gif = random.randint(1,9)
print(input("按回车开始抽奖！"))
if 1 <= gif <= 3 :
        print("恭喜您抽中一张机械革命9折优惠券！")
        xz = 0
        zk = 0.9
elif 3 <= gif <= 7:
            print("恭喜您抽中一张老干妈1优惠券！")
            xz = 5
            zk = 0.1
elif 7<= gif <= 9:
            print("恭喜您抽中一张辣条2折优惠券！")
            xz = 6
            zk = 0.2
else:
            print("您未抽到优惠券")
            sys.exit(0)






# 1.准备商品
shop = [
    ["机械革命",9000],  # shop[chose][1]
    ["Think pad",4500],
    ["Mac book pro",12000],
    ["手机",2000],
    ["可乐",3],
    ["老干妈",15],
    ["卫龙辣条",4]
]
# 2.准备足够的钱
money = input("请输入初始余额：")
money = int(money) # "5" --> 5



# 3.准备空的购物车
mycart = []




# 4.开始购物：

while True: # 死循环
    # 展示商品
    for key ,value in enumerate(shop):
        print(key,value)

    # 输入
    chose = input("请输入您想要的商品编号：")
    if chose.isdigit():# "5" --> 5
        chose = int(chose)
        # 商品是否存在
        if chose  > len(shop): # len()
            print("对不起，您输入商品不存在！别瞎弄！")
        else:
            if chose == xz:
                money1 =shop[chose][1]*zk
                money = money - money1
                print("恭喜，成功添加购物车!,您的余额还剩：￥",money)
            else :
                money = money - shop[chose][1]
                print("恭喜，成功添加购物车!,您的余额还剩：￥",money)




            # 金钱是否足够
            if money < shop[chose][1]:
                print("穷鬼，对不起，钱不够，到其他地方买去！")
            # else:
            #     mycart.append(shop[chose])
            #     money =  money - shop[chose][1]
            #     print("恭喜，成功添加购物车!,您的余额还剩：￥",money)

    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！拜拜了您嘞！")
        break
    else:
        print("对不起，输入非法，请重新输入！别瞎弄！")

# 打印购物小条
print("以下是您的购物小条，请拿好：")
print("--------------Jason 商城------------------")
for key ,value in enumerate(mycart):
    print(key,value)
print("您的钱包余额还剩：￥",money)
print("-----------------------------------------")






















































