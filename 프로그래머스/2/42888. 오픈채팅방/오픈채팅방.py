# 누군가 들어오면, "[닉네임]님이 들어왔습니다."
# 누군가 나가면, "[닉네임]님이 나갔습니다."
# <닉네임 변경 방법>
# 채팅방을 나간 후, 새로운 닉네임으로 다시 들어감.
# 채팅방에서 닉네임을 변경
# 닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경됨. 
# record : 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열
# 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 출력

def solution(record):
    members = {}
    answer = []
    
    # 최종 닉네임 구하는 반복문
    for rec in record :
        chat = rec.split(" ")
        if chat[0] != "Leave":
            members[chat[1]] = chat[2]
            
    # 메시지 출력
    for r in record:
        chat = r.split(" ")
        if chat[0] == "Enter":
            answer.append(members[chat[1]] + "님이 들어왔습니다.")
        elif chat[0] == "Leave":
            answer.append(members[chat[1]] + "님이 나갔습니다.")
    
    return answer
    