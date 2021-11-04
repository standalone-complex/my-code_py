#先算出等量是多少然后找到少于和大于的就行

T = int(input())

while T:
    Map = {}
    sum = 0
    name1 = ""
    name2 = ""
    while T:
        l = input().split()
        Map[l[-1]] = int(l[0]) * int(l[1]) * int(l[2])
        T -= 1
    
    for i in Map.values():
        sum += int(i)

    sum /= len(Map)

    for i in Map.items():
        if i[1] < sum:
            name1 = i[0]
        if i[1] > sum:
            name2 = i[0]
    
    print(name2 + " took clay from " + name1 + ".")

    T = int(input())
    if T == -1:
        break

