def solution(numbers, hand):
    answer = '' # 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타냄.
    cur_left = '*'
    cur_right = '#'
    key_pos = {1: (0,0), 2: (0,1), 3: (0,2),
              4: (1,0), 5: (1,1), 6: (1,2),
              7: (2,0), 8: (2,1), 9: (2,2),
              '*': (3,0), 0: (3,1), '#': (3,2)}
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            cur_left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            cur_right = number
        elif number in [2, 5, 8, 0]:
            target_pos = key_pos[number]
            left_pos = key_pos[cur_left]
            right_pos = key_pos[cur_right]
            
            dist_l = abs(target_pos[0] - left_pos[0]) + abs(target_pos[1] - left_pos[1])
            dist_r = abs(target_pos[0] - right_pos[0]) + abs(target_pos[1] - right_pos[1])
            
            if dist_l > dist_r:
                answer += 'R'
                cur_right = number
            elif dist_l < dist_r:
                answer += 'L'
                cur_left = number
            else:
                if hand == "left":
                    answer += 'L'
                    cur_left = number
                else:
                    answer += 'R'
                    cur_right = number
    return answer