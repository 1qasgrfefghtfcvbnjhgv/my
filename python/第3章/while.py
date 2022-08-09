total = 0
gird = 1
num = 1
while gird <=64:
    total += num
    gird += 1
    num *= 2
print("棋盘上的米粒总数："+str(total))
