# 고객만족도 설문지에는 고객이 이용했던 접수 창구번호와 정비 창구번호가 있음.
# 차량 정비소에는 N개의 접수 창구와 M개의 정비 창구가 있음.
# 첫 번째 단계 : 접수 창구에서 고장 접수
# 두 번째 단계 : 정비 창구에서 차량을 정비
# ai : 접수 창구 i에서 고객 한 명의 고장을 접수하는 데 걸리는 처리 시간
# bj : 정비 창구 j에서 고객 한 명의 차량을 정비하는 데 걸리는 처리 시간
# 차량 정비소를 방문한 고객 K명
# 고객번호 k의 고객이 차량 정비소에 도착하는 시간 tk
# 빈 접수 창구가 없는 경우 생길 때까지 기다림.
# 여러 고객이 기다리고 있는 경우 고객번호가 낮은 순서대로 우선 접수
# 빈 창구가 여러 곳인 경우 접수 창구번호가 작은 곳으로
# 지갑을 분실한 고객과 같은 접수 창구와 같은 정비 창구를 이용한 고객의 고객번호들을 찾아 그 합을 출력
# 만약, 그런 고객이 없는 경우 -1 출력

from collections import deque
import heapq

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    # N : 접수 창구 개수, M : 정비 창구 개수, K : 고객 수, A : 지갑을 두고 간 고객이 이용한 접수 창구번호, B : 정비 창구번호
    N, M, K, A, B = map(int, input().split()) 
    receipt_time = list(map(int, input().split())) # 접수 창구에서 접수하는 데 걸리는 시간
    repair_time = list(map(int, input().split())) # 정비 창구에서 정비하는 데 걸리는 시간
    visit_time = list(map(int, input().split())) # k번째 고객이 차량 정비소를 방문하는 시간

    wait_receipt = deque() # 접수 대기 큐, 고객 id 저장
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
                    heapq.heappush(wait_repair, (t, i+1, customer))
                    reception[i] = None

        # 3. 정비 창구 배정 (창구번호 작은 순)
        for j in range(M):
            if repair[j] is None and wait_repair:
                _, recp_no, customer = heapq.heappop(wait_repair)
                used_B[customer] = j + 1
                repair[j] = (customer, repair_time[j])

        # 4. 시간 t에 도착한 고객 -> 접수 대기열
        while idx < K and visit_time[idx] == t:
            wait_receipt.append(idx + 1)
            idx += 1

        # 5. 접수 창구 배정 (창구번호 작은 순)
        for i in range(N):
            if reception[i] is None and wait_receipt:
                customer = wait_receipt.popleft()
                used_A[customer] = i + 1
                reception[i] = (customer, receipt_time[i])

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