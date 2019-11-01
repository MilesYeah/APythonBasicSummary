
def addadd(num1):
    def add(num2):
        return num1 + num2
    return add

a1 = addadd(10)     # 10为传入到addadd中的参数
a2 = addadd(20)

print(a1(100))      # 100 为传入到add中的参数
print(a2(100))
