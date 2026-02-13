# 10 * 10 영역의 지도
# 같은 영역에 두 개의 배터리 충전기가 있다면 두 개 중 하나 선택해도 되고 하나를 나눠 써도 됨.
# BC의 정보와 사용자의 이동 궤적이 주어졌을 때, 모든 사용자가 충전한 양의 합의 최댓값 구하기
# 사용자 2명, 사용자 A는 지도의 (1, 1) 지점에서, 사용자 B는 지도의 (10, 10) 지점에서 출발

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    M, A = map(int, input().split()) # M : 총 이동 시간, A : BC의 개수
    A_move = list(map(int, input().split())) # 사용자 A의 이동 정보
    B_move = list(map(int, input().split())) # 사용자 B의 이동 정보
    BC = [list(map(int, input().split())) for _ in range(A)] # X, Y 좌표, 충전 범위(C), 처리량(P)