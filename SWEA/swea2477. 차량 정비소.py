# 차량 정비소에는 N개의 접수 창구와 M개의 정비 창구가 있음.
# 첫 단계 : 접수 창구에서 고장 접수
# 두 번째 단계 : 정비 창구에서 차량 정비
# 차량 정비가 끝난 고객은 고객만족도 설문지를 받음.
# 접수 창구 및 정비 창구의 담당자 업무 능력이 달라서 담당자 별 처리 시간이 다름.
# ai : 접수 창구 i에서 고객 한 명의 고장을 접수하는 데 걸리는 처리 시간
# bj : 정비 창구 j에서 고객 한 명의 차량을 정비하는 데 걸리는 처리 시간
# 지금까지 차량 정비소를 방문한 고객은 K명
# 고객번호 k의 고객이 차량 정비소에 도착하는 시간 : tk
# 빈 접수 창구가 있는 경우 빈 접수 창구에 가서 고장을 접수 / 없으면 빈 접수 창구가 생길 때까지 기다림.
# 빈 정비 창구가 있는 경우 빈 정비 창구에 가서 정비를 받음 / 없으면 빈 정비 창구가 생길 때까지 기다림.
# 접수 창구의 우선순위 : 여러 고객이 기다리고 있는 경우 고객번호가 낮은 순서대로 우선 접수 / 빈 창구가 여러 개인 경우 접수 창구번호가 작은 곳으로
# 정비 창구의 우선순위 : 먼저 기다리는 고객 우선 / 두 명 이상의 고객이 동시에 정비 창구로 이동하면 이용했던 접수 창구번호가 작은 고객 우선 / 빈 창구가 여러 곳이면 정비 창구번호가 작은 곳으로
# 이동 시간 0
# 지갑을 분실한 고객과 같은 접수 청구와 같은 정비 창구를 이용한 고객의 고객번호들을 찾아 그 합을 출력
# 만약 그런 고객이 없는 경우 -1 출력
# 창구번호와 고객번호는 1부터 시작

from collections import deque
import heapq

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    # N : 접수 창구의 개수, M : 정비 창구의 개수, K : 차량 정비소를 방문한 고객의 수, A : 지갑을 두고 간 고객이 이용한 접수 창구번호, B : 정비 창구번호
    N, M, K, A, B = map(int, input().split())
    reception_time = list(map(int, input().split())) # i번째 접수 창구가 고장을 접수하는 데 걸리는 시간 ai가 N개 주어짐.
    repair_time = list(map(int, input().split())) # j번째 정비 창구가 차량을 정비하는 데 걸리는 시간 bj가 M개 주어짐.
    arrive = list(map(int, input().split())) # k번째 고객이 차량 정비소를 방문하는 시간 tk가 순서대로 K개 주어짐.

    wait_recep = deque() # 접수 대기 큐, 고객 id 저장
    wait_repair = [] # 정비 대기 큐, (접수 완료 시각, 접수창구번호, 고객 id)

    reception = [None] * N # 접수 창구 상태 배열, (누가 쓰는지, 남은 시간)
    repair = [None] * M # 정비 창구 상태 배열, (누가 쓰는지, 남은 시간)

    used_A = [0] * (K + 1) # 어떤 고객이 몇 번 접수 창구를 이용했는가 => A랑 비교
    used_B = [0] * (K + 1) # 어떤 고객이 몇 번 정비 창구를 이용했는가 => B랑 비교

    t = 0 # 시간
    idx = 0 # 아직 도착 처리 안 한 고객 인덱스
    done = 0 # 정비 끝난 고객
    answer = 0 # A, B를 이용한 고객번호의 합

    while done < K:
        # 1. 정비 완료 처리
        for j in range(M):
            if repair[j] is not None:
                customer, remain = repair[j]
                if remain == 0:
                    # 정비 완료 -> 설문지 받음(종료)
                    if used_A[customer] == A and used_B[customer] == B:
                        answer += customer
                    repair[j] = None
                    done += 1
        
        # 2. 접수 완료 고객을 정비 대기로 이동
        for i in range(N):
            if reception[i] is not None:
                customer, remain = reception[i]
                if remain == 0:
                    # 시간 t에 접수 완료 -> 정비 대기열로
                    heapq.heappush(wait_repair, (t, i + 1, customer))
                    reception[i] = None

        # 3. 정비 창구 배정 (창구번호 작은 순)
        for j in range(M):
            if repair[j] is None and wait_repair:
                _, recp_no, customer = heapq.heappop(wait_repair)
                used_B[customer] = j + 1
                repair[j] = (customer, repair_time[j])

        # 4. 시간 t에 도착한 고객 -> 접수 대기열
        while idx < K and arrive[idx] == t:
            wait_recep.append(idx + 1)
            idx += 1

        # 5. 접수 창구 배정 (창구번호 작은 순)
        for i in range(N):
            if reception[i] is None and wait_recep:
                customer = wait_recep.popleft()
                used_A[customer] = i + 1
                reception[i] = (customer, reception_time[i])

        # 6. 1초 경과: 남은 시간 감소
        for i in range(N):
            if reception[i] is not None:
                customer, remain = reception[i]
                reception[i] = (customer, remain - 1)

        for j in range(M):
            if repair[j] is not None:
                customer, remain = repair[j]
                repair[j] = (customer, remain - 1)

        t += 1

    if answer == 0:
        answer = -1

    print(f'#{test_case} {answer}')