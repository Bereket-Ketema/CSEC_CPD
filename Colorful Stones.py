string1=input()
string2=input()
count=1
j=0
for i in range(len(string2)):
  if string2[i]==string1[j]:
    count+=1
    j+=1
print(count)
