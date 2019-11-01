
## 重新实现str.strip()
def rightStrip(tempStr,splitStr):
    endindex = tempStr.rfind(splitStr)
    while endindex != -1 and endindex == len(tempStr) - 1:
         tempStr = tempStr[:endindex]
         endindex = tempStr.rfind(splitStr)
    return tempStr

def leftStrip(tempStr,splitStr):
    startindex = tempStr.find(splitStr)
    while startindex == 0:
        tempStr = tempStr[startindex+1:]
        startindex = tempStr.find(splitStr)
    return tempStr

str = "  H  "
print(str)
print(leftStrip(str,' '))
print(rightStrip(str,' '))

"""
#输出
  H  
H  
  H
"""
