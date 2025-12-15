# swea 1940. 가랏! RC카!
T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N = int(input()) # Command의 수
    answer = 0 # N초 동안 이동한 거리
    cur_speed = 0 # 현재 속도

    for n in range(N):
        command = list(map(int, input().split()))

        if command[0] == 1:
            cur_speed += command[1]
        elif command[0] == 2:
            cur_speed -= command[1]
            if cur_speed < 0:
                cur_speed = 0
        
        answer += cur_speed

    print(f'#{test_case} {answer}')