# 기존에는 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공
# 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성 
# 단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
# 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함
# orders : 각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열
# course : 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 
# 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 출력 

from itertools import combinations

def solution(orders, course):
    answer = [] # 새로 추가하게 될 코스요리의 메뉴 구성 
    
    for c in course:
        menu_comb = {} # 메뉴 조합별로 몇 명이 주문했는가
        
        for order in orders:
            for comb in combinations(sorted(order), c):
                if comb not in menu_comb:
                    menu_comb[comb] = 0
                
                menu_comb[comb] += 1
                
        if menu_comb:
            max_count = max(menu_comb.values())
            
            if max_count >= 2:
                for comb, count in menu_comb.items():
                    if count == max_count:
                        answer.append(''.join(comb))
            
    return sorted(answer)