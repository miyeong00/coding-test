# 트럭 여러 대가 일차선 다리를 정해진 순서대로 건널 거임.
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는가 
# 다리에는 트럭이 최대 bridge_length대 올라갈 수 있음.
# 다리는 weight 이하까지의 무게를 견딜 수 있음.
# bridge_length : 다리에 올라갈 수 있는 트럭 수
# weight : 다리가 견딜 수 있는 무게
# truck_weights : 트럭 별 무게 

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length) # 다리
    truck_weights = deque(truck_weights) # 대기 중인 트럭
    answer = 0 # 모든 트럭이 다리를 건너기 위해 걸린 시간
    
    while truck_weights:
        answer += 1 # 1초 경과
        bridge.popleft() # 다리 맨 앞 제거
        
        if sum(bridge) + truck_weights[0] <= weight:
            truck = truck_weights.popleft() # 젤 처음 대기 중인 트럭 제거
            bridge.append(truck)
        else:
            bridge.append(0)
            
    return answer + bridge_length