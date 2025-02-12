y,w =map(int,input().split())
a= 6 - max(y,w)+1
b = 6
if a % 2 == 0:
  a //= 2;b //= 2  
if a % 3 == 0:
  a //= 3;b //= 3  
print("{}/{}".format(a,b))
