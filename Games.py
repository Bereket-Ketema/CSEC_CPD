n=int(input())
team=[]
count=0
for i in range(n):
  nums=list(map(int,input().split(" ")))
  team.append(nums)
for i in range(n):
  for j in range(n):
   count+=1 if i!=j and team[i][0]==team[j][1] else 0  
print(count)
