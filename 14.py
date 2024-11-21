a, b = map(int, input().split())
c = input()
c = int(c)
m = b+c
if (m >= 60) :
    a += m/60
    if a >= 24 : a = 0
    
    m = m%60
    print("%d "%a, end="")
    print("%d"%m)

else :
    print("%d "%a, end="")
    print("%d"%m)