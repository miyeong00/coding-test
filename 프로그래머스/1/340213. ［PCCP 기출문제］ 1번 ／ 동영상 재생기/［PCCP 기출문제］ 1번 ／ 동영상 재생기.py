# 동영상 재생기 기능 : 10초 전으로 이동, 10초 후로 이동, 오프닝 건너뛰기
# 10초 전으로 이동 : "prev"를 입력하면 현재 위치에서 10초 전으로 이동. 현재 위치가 10초 미만인 경우 0분 0초로 이동
# 10초 후로 이동 : "next" 입력하면 현재 위치에서 10초 후로 이동. 남은 시간이 10초 미만일 경우 마지막 위치
# 오프닝 건너뛰기 : 현재 재상 위치가 오프닝 구간인 경우 자동으로 오프닝이 끝나는 위치로 이동 
# video_len : 동영상의 길이
# pos : 기능이 수행되기 직전의 재생위치를 나타내는 문자열
# op_start : 오프닝 시작 시각 문자열
# op_end : 오프닝 끝나는 시각 문자열
# commands : 사용자 입력을 나타내는 문자열 배열
# 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 출력

def minute_to_second(t):
    minute, second = map(int, t.split(":"))
    return minute * 60 + second

def solution(video_len, pos, op_start, op_end, commands):
    video_len = minute_to_second(video_len)
    pos = minute_to_second(pos)
    op_start = minute_to_second(op_start)
    op_end = minute_to_second(op_end)
    
    if op_start <= pos <= op_end:
        pos = op_end

    for command in commands:
        if command == 'prev':
            pos = max(pos - 10, 0)
        else:
            pos = min(pos + 10, video_len)
                
        if op_start <= pos <= op_end:
            pos = op_end
                
    return f"{pos // 60:02d}:{pos % 60:02d}"
    
    