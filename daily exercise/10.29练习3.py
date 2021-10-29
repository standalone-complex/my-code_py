
T= int(input())

for i in range(T):
    flag = False
    n = int(input())
    ls = []

    for j in range(n):
        l = list(map(int, input().split()))
        ls.append(l)

    for p in range(n):
        for q in range(p, n):
            if ls[p][q] != ls[q][p]:
                flag = True
                break
        if(flag == True):
            break
    
    if flag:
        print("No")
    else:
        print("Yes")

