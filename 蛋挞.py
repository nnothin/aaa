from threading import Thread
import time
count = 0   #篮子里的蛋挞数量
money = 3000  #金额

class cooker(Thread):   #厨师
    cookname = " "              #厨师名
    make_num = 0                #做出的蛋挞数量
    def run(self) -> None:
        global count            #使用全局变量 count
        while True:
            if count < 500 and count >= 0:
                self.make_num = self.make_num+1
                count = count + 1
                print(self.cookname,"做出蛋挞")
            elif count == 500:
                print("篮子已满")
                time.sleep(3)
            elif count == 500 and money == 0:
                # print("一共做了",count,"个")
                break

# class shoppgod(Thread):             #消费者
#     shoppgod_name = " "   #消费者
#     get_num = 0     #购买数量
#     global money
#     global count
#     def run(self) -> None:
#         while True:
#             if count > 0 and money > 0:
#                 self.get_num = self.get_num + 1
#                 count = count - 1
#                 money = money - 2
#                 print(self.shoppgod_name,"买了",self.get_num,"个")
#             elif  count == 0 and money > 0:
#                 time.sleep(2)
#                 print("暂无存货，等待片刻...")
#             elif money <= 0:
#                 print("没钱滚蛋！")



class shop(Thread):  #消费
    def run(self) -> None:
        global count
        global money
        while True:
            if count > 0 and money > 0:
                count = count - 1
                money = money - 2
                print("购买了一个蛋挞")
            elif count == 0:
                print("篮子空了，等等")
                time.sleep(2)
            elif money == 0:
                break



c1 = cooker()
# c1.cookname = "A"

c2 = cooker()
# c2.cookname = "B"

c3 = cooker()
# c3.cookname = "C"

c1.start()
c2.start()
c3.start()


s1 = shop()
# s1.shoppgod_name = "nana"

s2 = shop()
# s2.shoppgod_name = "kaka"

s3 = shop()
# s3.shoppgod_name = "haha"

s1.start()
s2.start()
s3.start()