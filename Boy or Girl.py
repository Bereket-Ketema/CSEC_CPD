string=input()
nums=[]
for i in range(len(string)):
  nums.append(string[i]) if(string[i] not in nums) else None
print("CHAT WITH HER!") if len(nums)%2==0 else print("IGNORE HIM!")
