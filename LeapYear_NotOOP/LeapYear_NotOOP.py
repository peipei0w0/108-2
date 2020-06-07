##西元年份除以4不可整除，為平年。
##西元年份除以4可整除，且除以100不可整除，為閏年。
##西元年份除以100可整除，且除以400不可整除，為平年
##西元年份除以400可整除，為閏年。
def isLeapYear(newYear):
    if (newYear % 400 == 0) or (newYear % 100 != 0 and newYear % 4 == 0):
        return True
    else:
        return False

for i in range(3):
    day=input()
    day=int(day)

    if(isLeapYear(day) == True):
        print("The",day,"is leap year.")
    else:print("The",day,"isn't leap year.")