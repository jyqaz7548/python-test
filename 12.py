import sys
s = input()
s = int(s)
i = 0
while i<s :
    i+=1
    a, b = map(int, input().split())
    su = a+b
    print("Case #",end="")
    print(i,end="")
    print(":%d"%su)

sys.exit(1)