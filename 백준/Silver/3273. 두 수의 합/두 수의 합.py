n = int(input()) # 수열의 크기
a = list(map(int, input().split())) # n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열
x = int(input()) # ai + aj = x 
checked = set()
cnt = 0
for num in a:
    if (x - num) in checked:
        cnt += 1
    checked.add(num)
print(cnt)