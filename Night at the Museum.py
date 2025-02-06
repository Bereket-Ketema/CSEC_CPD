string=input()
alpha=ord('a')
find=0
for i in string:
    big =abs(ord(i)-alpha)
    find+=min(big,26-big)
    alpha=ord(i)
print(find)
