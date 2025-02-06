n=int(input())
amount=list(map(int,input().split()))
crime,officer=0,0
for i in range(n):
  if amount[i] !=-1:
    officer+=amount[i]
  elif amount[i] ==-1:
    if officer>0:
      crime+=0
      officer-=1
    else:
      crime+=1    
print(crime)
