# 일정한 금액을 지불하면 10일 동안 회원 자격을 부여함.
# 회원을 대상으로 매일 한 가지 제품을 할인. 하루에 하나씩만 살 수 있음.
# 정현이는 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입을 할거임.
# want : 정현이가 원하는 제품을 나타내는 문자열 배열
# number : 정현이가 원하는 제품의 수량을 나타내는 정수 배열
# discount : XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열
# 회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수 출력 
# 가능한 날이 없으면 0 출력 

def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - sum(number) + 1):
        sale = discount[i : i+sum(number)]
        
        for idx in range(len(want)):
            if sale.count(want[idx]) != number[idx]:
                break
        else:
            answer += 1       
    
    return answer
        
        
    