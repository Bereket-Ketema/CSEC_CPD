n=int(input())
nums=list(map(int,input().split( )))
nums.sort()
for value in nums:
  print(value,end=" ")
