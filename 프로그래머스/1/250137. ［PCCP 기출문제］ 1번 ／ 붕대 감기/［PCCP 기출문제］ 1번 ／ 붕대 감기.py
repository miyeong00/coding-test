# 붕대 감기는 t초 동안 붕대를 감으면서 1초마다 x만큼의 체력을 회복함.
# t초 연속으로 붕대를 감는 데 성공한다면 y만큼의 체력을 추가로 회복
# 게임 캐릭터에는 최대 체력이 존재해 현재 체력이 최대 체력보다 커지는 것은 불가능
# 기술을 쓰는 도중 몬스터에게 공격을 당하면 기술이 취소되고, 공격을 당하는 순간에는 체력을 회복할 수 없음.
# 몬스터에게 공격당해 기술이 취소당하거나 기술이 끝나면 그 즉시 붕대 감기를 다시 사용하며, 연속 성공 시간이 0으로 초기화됨.
# 몬스터의 공격을 받으면 정해진 피해량만큼 현재 체력이 줄어듦.
# 현재 체력이 0 이하가 되면 캐릭터가 죽으면 더 이상 체력을 회복할 수 없음.
# bandage : 붕대 감기 기술의 시전 시간, 1초당 회복량, 추가 회복량을 담은 1차원 정수 배열
# health : 최대 체력을 의미하는 정수
# attacks : 몬스터의 공격 시간과 피해량을 담은 2차원 정수 배열
# 모든 공격이 끝난 직후 남은 체력 출력
# 만약 몬스터의 공격을 받고 캐릭터의 체력이 0 이하가 되어 죽으면 -1 출력

def solution(bandage, health, attacks):
    t = 0 # 현재 시간
    success = 0 # 연속 성공 시간
    idx = 0 # attacks 배열의 몇 번째 공격까지 진행되었는지 확인하는 인덱스
    max_health = health # 최대 체력
    
    skill = bandage[0] # 붕대 감기 기술의 시전 시간
    recovery = bandage[1] # 1초당 회복량
    addition = bandage[2] # 추가 회복량
    
    for t in range(1, attacks[-1][0] + 1):
        if idx < len(attacks) and t == attacks[idx][0]:
            health -= attacks[idx][1]
            success = 0
            idx += 1
            
            if health <= 0:
                return -1
        else:
            health += recovery
            success += 1
            
            if success == skill:
                health += addition
                success = 0
                
            if health > max_health:
                health = max_health
                
    return health
        