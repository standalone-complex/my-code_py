str = input()
#壹亿贰仟叁佰肆拾伍万陆仟柒佰捌拾玖圆
ret = ""

flag1 = 0
flag2 = 0

for num in reversed(str):
    if flag1 == 0:
        if flag2 == 0:
            ret += "圆"
        elif flag2 == 1:
            ret += "万"
        elif flag2 == 2:
            ret += "亿"
    elif flag1 == 1:
        ret += "拾"
    elif flag1 == 2:
        ret += "佰"
    elif flag1 == 3:
        ret += "仟"

    if num == "0":
        ret += "零"
    elif num == "1":
        ret += "壹"
    elif num == "2":
        ret += "贰"
    elif num == "3":
        ret += "叁"
    elif num == "4":
        ret += "肆"
    elif num == "5":
        ret += "伍"
    elif num == "6":
        ret += "陆"
    elif num == "7":
        ret += "柒"
    elif num == "8":
        ret += "捌"
    elif num == "9":
        ret += "玖"
    flag1 = (flag1+1) % 4
    if flag1 == 0:
        flag2 += 1

for i in reversed(ret):
    print(i.rstrip().strip(), end = "")