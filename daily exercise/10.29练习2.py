def solve(n, m, a):
    ans = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == max(a[i]) and a[i][j] <= min(l[j] for l in a):
                print(a[i][j], i, j)
                ans += 1
    return ans

while True:
    try:
        n, m = map(int, input().split())
        a = []
        for i in range(n):
            l = list(map(int, input().split()))
            a.append(l)
        if solve(n, m, a) == 0:
            print("Not")
    except:
        break