string=input()
upp,low=0,0
for i in range(len(string)):
  if string[i].isupper():
    upp+=1
  else:
    low+=1
print(string.upper()) if upp>low else print(string.lower())
