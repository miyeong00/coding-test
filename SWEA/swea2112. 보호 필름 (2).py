# 보호 필름은 엷은 투명한 막을 D장 쌓아서 제작됨.
# 막은 동일한 크기를 가진 바 모양의 셀들이 가로 방향으로 W개 붙여서 만들어짐.
# ==> 두께 D, 가로 크기 W의 보호 필름
# 각 셀들은 특성 A 또는 특성 B를 가지고 있음.
# 보호 필름의 성능을 검사하기 위한 합격기준 K
# 단면의 모든 세로방향에 대해서 동일한 특성의 셀들이 K개 이상 연속적으로 있는 경우에만 성능검사를 통과하게 됨.
# 성능검사에 통과하기 위해서 약품을 사용해야 함. => 특정 막에 약품 A를 투입하면 막 내의 모든 셀들이 특성 A로 변경되며, 약품 B를 넣으면 모두 특성 B로 변경됨.
# 약품 투입 횟수를 최소로 하여 성능검사를 통과할 수 있는 방법을 찾고, 이때의 약품 투입 횟수 출력
# 약품을 투입하지 않고도 성능검사를 통과하는 경우에는 0 출력
# 특성 A : 0, 특성 B : 1

# 성능 검사 함수
# 모든 열에 대해 같은 값이 K개 이상 연속으로 존재하면 통과
# 한 열이라도 K 연속을 못 만들면 즉시 실패
def check():
    for col in range(W):
        cur = 1 # 현재 열에서 연속 개수
        prev = films[0][col] # 현재 열에서 직전 값, 일단 초기값은 첫번째 행

        # 이 열이 K 연속을 만족했는가
        ok = False

        # 세로 방향 검사
        for row in range(1, D):
            if films[row][col] == prev: # 현재 값과 직전값이 같으면 연속 개수 +1
                cur += 1
            else: # 현재 값과 직전값이 다르면 연속 개수랑 직전값 초기화
                prev = films[row][col]
                cur = 1

            # K개 이상 연속이 되면, 이 열은 통과 처리
            if cur >= K:
                ok = True
                break

        # 끝까지 봤는데도 K개 이상 연속이 아니면 통과 X
        if not ok:
            return False
        
    # 모든 열이 ok면 전체 합격
    return True



# row : 현재 행, cnt : 지금까지의 약품 투입 횟수
# 백트래킹
#    1. 그대로 둔다
#    2. 약품 A 투입 -> 해당 행 전체를 0으로 변경
#    3. 약품 B 투입 -> 해당 행 전체를 1로 변경
def dfs(row, cnt):
    # 가지치기 : 이미 현재 cnt가 answer 이상이면, 더 진행해도 최소값 갱신할 수 없음. => 중단
    global answer
    if cnt >= answer:
        return
    
    # 종료조건 : 모든 행을 전부 결정했을 때 이제 완성된 필름으로 성능검사 수행
    if row == D:
        if check():
            answer = min(answer, cnt)
        return
    
    # 1. 현재 행을 그대로 두고 다음 행으로
    dfs(row + 1, cnt)

    # 현재 행 원본 백업
    backup = films[row][:]

    # 2. 약품 A 투입
    films[row] = [0] * W
    dfs(row + 1, cnt + 1)

    # 3. 약품 B 투입
    films[row] = [1] * W
    dfs(row + 1, cnt + 1)

    # 복구
    films[row] = backup

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    D, W, K = map(int, input().split()) # D : 보호 필름의 두께, W : 가로크기, K : 합격기준
    films = [list(map(int, input().split())) for _ in range(D)] # D줄에 셀들의 특성 W개가 주어짐.

    # K == 1이면 무조건 통과
    if K == 1:
        print(f'#{test_case} 0')
        continue

    answer = D

    # 약품 없이도 통과하면 0
    if check():
        print(f'#{test_case} 0')
        continue

    dfs(0, 0)
    print(f'#{test_case} {answer}')