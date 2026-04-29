x,y=map(str,input().split())
if x[::-1]<y[::-1]:
    print(y[::-1])
else:
    print(x[::-1])
