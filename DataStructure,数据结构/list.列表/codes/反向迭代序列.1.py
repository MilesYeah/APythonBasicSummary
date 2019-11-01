

#如果是一个list,最快的方法使用reverse
tempList = [1,2,3,4]
tempList.reverse()
for x in tempList:
    print(x)



templist = [1,2,3,4]
for i in templist[::-1]:
    print(templist[i])



#如果不是list,需要手动重排
templist = (1,2,3,4)
for i in range(len(templist)-1,-1,-1):
    print(templist[i])

