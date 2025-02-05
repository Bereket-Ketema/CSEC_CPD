n=int(input())
numbers=[]
for i in range(n):
  nums=list(map(int,input().split( )))
  numbers.append(nums)
sum,check=0,0
for j in range(len(numbers)):
  for i in range(3):
    if numbers[j][i]==1:
      check+=1  
  if check>=2:
    sum+=1
  check=0
print(sum)   
