ynum = (10+69+140+10+10)
yprice = ynum*253.6
tnum = (63+45+129+63+58+48+63)
tprice = tnum*65.8
cnum = 120
cprice = cnum*49.3
fnum = (43+25+43+60+43+78)
fprice = fnum*96.8
nnum = (60+72+35+90+60+60+140)
nprice = nnum*86.3
pnum = (63+24+63+57)
pprice = pnum*135.9
snum = (ynum+tnum+cnum+fnum+nnum+pnum+fnum)
sum  = (yprice+tprice+cprice+fprice+nprice+pprice)
avg = sum/30
print("总销售额为：",sum)
print("平均每日销售数量为：",avg)
print("羽绒服月销售占比为{:.2f} %".format(ynum/snum * 100))
print("T恤月销售占比为"'%.2f%%' % (tnum/snum * 100))
print("衬衫月销售占比为"'%.2f%%' % (cnum/snum * 100))
print("风衣月销售占比为"'%.2f%%' % (fnum/snum * 100))
print("牛仔裤月销售占比为"'%.2f%%' % (nnum/snum * 100))
print("皮草月销售占比为"'%.2f%%' % (pnum/snum* 100))