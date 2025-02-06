numbers=list(map(int,input().split()))
string=input()
game=0
for i in range(len(string)):
    game+=numbers[0]  if string[i]=='1' else(numbers[1] if string[i]=='2' else(numbers[2] if string[i]=='3' else numbers[3]))
print(game)
