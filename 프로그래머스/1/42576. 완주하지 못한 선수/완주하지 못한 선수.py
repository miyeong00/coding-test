# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주함.
# participant : 마라톤에 참여한 선수들의 이름이 담긴 배열
# completion : 완주한 선수들의 이름이 담긴 배열
# 완주하지 못한 선수의 이름 출력

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]