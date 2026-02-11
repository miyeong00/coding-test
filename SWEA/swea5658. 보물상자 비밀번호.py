# 각 변에 16진수 숫자(0~F)가 적혀 있는 보물상자가 있음.
# 보물상자의 뚜껑은 시계방향으로 돌릴 수 있고, 한 번 돌릴 때마다 숫자가 시계방향으로 한 칸씩 회전
# 각 변에는 동일한 개수의 숫자가 있고, 시계방향 순으로 높은 자리 숫자에 해당하며 하나의 수를 나타냄.
# 보물상자에는 자물쇠가 걸려있는데,
# 이 자물쇠의 비밀번호는 보물상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진수로 만든 수
# N개의 숫자가 입력으로 주어졌을 때, 보물상자의 비밀 번호를 출력
# 서로 다른 회전 횟수에서 동일한 수가 중복으로 생성될 수 있음. 크기 순서를 셀 때 같은 수를 중복으로 세지 않도록 주의

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N, K = map(int, input().split()) # N : 숫자의 개수, K : 크기 순서
    treasure = input() # N개의 숫자
    L = N // 4 # 회전 횟수

    answer = set() # 회전할 때마다 생성되는 숫자 담는 집합 -> 중복 제거해줌.

    # L번 회전 실시
    for _ in range(L):
        answer.add(treasure[0:L])
        answer.add(treasure[L:2*L])
        answer.add(treasure[2*L:3*L])
        answer.add(treasure[3*L:4*L])

        # 회전
        treasure = treasure[-1] + treasure[:-1]

    # 16진수를 10진수로 변환해서 리스트로 만들기
    lst = []
    for a in answer:
        lst.append(int(a, 16))

    # 내림차순 정렬
    lst.sort(reverse=True)

    # K번째 출력
    print(f'#{test_case} {lst[K-1]}')

    