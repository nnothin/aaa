# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# 1、请循环遍历出所有的key
# for i in range(1):
#     print(dict.keys())

# 2、请循环遍历出所有的value
# for i in range(1):
#     print(dict.values())

# 3、请在字典中增加一个键值对，“k4:v4”
# dict1 = {"k4":"v4"}
# dict.update(dict1)
# print(dict)

# 4、小明去超市购买水果，账单如下：
# 苹果 32.8
# 香蕉 22
# 葡萄 15.5
# 请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用，用水果名称做key，金额做value，创建一个字典
# info = {"苹果":32.8,
#         "香蕉":22,
#         "葡萄":15.5
# }
# print(info)


# 小明，小刚去超市里购买水果
# 小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
# 以姓名做key，value仍然是字典
# friuts = {
#     "苹果":12.3,
#     "草莓":4.5,
#     "香蕉":6.3,
#     "葡萄":5.8,
#     "橘子":6.4,
#     "樱桃":15.8
# }
# info = {
#     '小明': {'fruits': {'苹果':4, '草莓':13, '香蕉':10},'money':  ""},
#     '小刚': {'fruits': {'葡萄':19, '橘子':12, '樱桃':30},'money': ""}
# }
# money1 = info['小明']['fruits']['苹果']* friuts['苹果'] + info['小明']['fruits']['草莓']* friuts['草莓']  + info['小明']['fruits']['香蕉']* friuts['香蕉']
# money2 = info['小刚']['fruits']['葡萄']* friuts['葡萄'] + info['小刚']['fruits']['橘子']* friuts['橘子']  + info['小刚']['fruits']['樱桃']* friuts['樱桃']
# ming = "￥170.7"
# gang = "￥661.0"
# info['小明']['money'] = ming
# info['小刚']['money'] = gang
# print(info)


# 5、编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）
import random
# def num(a):
#     sz = {}
#     for i in a:
#         if i not in sz:
#             sz[i] = 1;
#         else:
#             sz[i] += 1
#     return sz
# list = [21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
# print(list)
# many = num(list)
# print(many)


# 6、有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# names = {'刘备':{'年龄':'56','性别':'男','编号':'106','任职公司':'IBM','薪资':500,'部门编号':'50'},
#                '大乔':{'年龄':'19','性别':'女','编号':'230','任职公司':'微软','薪资':501,'部门编号':'60'},
#                '小乔':{'年龄':'19','性别':'女','编号':'210','任职公司':'Oracle','薪资':600,'部门编号':'60'},
#                '张飞':{'年龄':'45','性别':'男','编号':'230','任职公司':'Tencent','薪资':700,'部门编号':'10'}
#                }
# print(names)






