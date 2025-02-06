n=int(input())
nums=list(map(int,input().split(" ")))
he,she=0,0
j=n-1
for i in range(n):
  if i%2==0:
    if nums[0]>=nums[j]:
      she+=nums[0]
      nums.pop(0)
      j-=1
    elif nums[0]<=nums[j]:
      she+=nums[j]
      nums.pop(j)
      j-=1
  else:
    if nums[0]>=nums[j]:
      he+=nums[0]
      nums.pop(0)
      j-=1
    elif nums[0]<=nums[j]:
      he+=nums[j]
      nums.pop(j)
      j-=1
print(she,he)
