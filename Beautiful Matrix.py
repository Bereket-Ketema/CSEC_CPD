numbers=[]
for i in range(5):
  nums=list(map(int,input().split( )))
  numbers.append(nums)
row,column=0,0
for j in range(5):
  if 1 in numbers[j]:
    for i in range(5):
      if numbers[j][i]==1:
        # print(f"index is ({j},{i})")
        row,column=j,i
        break   
if row==0 or row==4:
  print(4) if column==0 or column==4 else(print(3) if column==1 or column==3 else print(2))
elif row==1 or row==3:
  print(3) if column==0 or column==4 else(print(2) if column==1 or column==3 else print(1))
elif row==2:
  print(2) if column==0 or column==4 else(print(1) if column==1 or column==3 else print(0))
