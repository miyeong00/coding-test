# 직원들은 일주일동안 자신이 설정한 '출근 희망 시각 + 10분'까지 어플로 출근해야 함.
# 토요일, 일요일의 출근 시각은 이벤트에 영향을 끼치지 않음.
# 모든 시각은 시에 100을 곱하고 분을 더한 정수로 표현됨.
# 직원들이 설정한 출근 희망 시각과 실제로 출근한 기록을 바탕으로 상품을 받을 직원이 몇 명인지 구하기
# schedules : 직원 n명이 설정한 출근 희망 시각을 담은 1차원 정수 배열
# timelogs : 직원들이 일주일 동안 출근한 시각을 담은 2차원 정수 배열
# startday : 이벤트를 시작한 요일을 의미하는 정수
# 1 - 월 / 2 - 화 / 3 - 수 / 4 - 목 / 5 - 금 / 6 - 토 / 7 - 일

def solution(schedules, timelogs, startday):
    answer = 0 # 상품을 받을 직원
    
    idx_sat = 6 - startday # 토요일 인덱스
    
    for i in range(len(schedules)):
        hope = schedules[i] # i번째 사람의 출근 희망 시각
        
        # i번째 사람의 출근 인정 시각
        if hope % 100 >= 50:
            okay = ((hope // 100) + 1) * 100 + (hope % 100) + 10 - 60
        else:
            okay = hope + 10
        
        is_success = True
        for j in range(7):
            current_day = (startday + j - 1) % 7 + 1

            if current_day >= 6:
                continue

            if timelogs[i][j] > okay:
                is_success = False
                break

        if is_success:
            answer += 1
                
    return answer