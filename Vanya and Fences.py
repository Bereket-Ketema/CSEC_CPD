n,h=map(int,input().split())
person=list(map(int,input().split()))
value=0
for i in person:
  value+=2 if i>h else 1
print(value)
