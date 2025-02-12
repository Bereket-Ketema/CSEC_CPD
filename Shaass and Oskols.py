n = int(input())
num = list(map(int, input().split()))
shout = int(input())
for _ in range(shout):
    a, b = map(int, input().split())
    a -= 1  
    if a > 0:
        num[a - 1] += b - 1
    if a < n - 1:
        num[a + 1] += num[a] - b
    num[a] = 0
for birds in num:
    print(birds)
