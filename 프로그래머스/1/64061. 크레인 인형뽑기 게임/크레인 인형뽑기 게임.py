# board : 게임 화면의 격자의 상태가 담긴 2차원 배열
# moves : 크레인을 작동시킨 위치가 담긴 배열
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수 출력

def solution(board, moves):
    answer = 0 # 터트려져 사라진 인형의 개수
    stack = [] # 뽑은 인형 모아놓을 바구니
    n = len(board)
    
    for m in moves:
        for i in range(n):
            if board[i][m-1] >= 1:
                if stack and stack[-1] == board[i][m-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][m-1])
                board[i][m-1] = 0
                break
                    
    return answer
    
    