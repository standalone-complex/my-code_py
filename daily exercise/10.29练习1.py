def Judge(n,m,ls):
    count = 0
    flag = 1
    for i in range(n):
        Max = max(ls[i])
        for j in range(n):
            if int(Max) > int(ls[j][ls[i].index(Max)]):
                flag = 0
        if flag == 1:
            for k in range(m):
                if int(Max)==int(ls[i][k]):
                    print(Max,i,k)
                    
            
        else:
            flag = 1
            count += 1
            if count == n:
                print("Not")
try:
    while True:
        n,m = map(int,input().split( ))
        ls = []
        for j in range(n):
            str1 = input()
            l1 = list(str1.split( ))
            ls.append(l1)
        for i in range(n):
            ls[i] = list(map(int,ls[i]))
        Judge(n,m,ls)
except EOFError:
    pass