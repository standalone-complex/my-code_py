from collections import OrderedDict

T = int(input())

while T:
    l = list(input().split())
    n = l[0]
    target_team = l[1]
    Map = OrderedDict()

    for i in n:
        a = list(input().split())

        if target_team == a[0]:
            target_count = a[1]
            target_score = a[2]

        Map[a[1]] = [a[2]]
    
    critical = int(len(Map) * 0.4)

    if int(Map[critical]) <= int(target_count) and int(Map[critical]) <= int(target_score):
        print("YES")
    else:
        print("NO")


    T -= 1