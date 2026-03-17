def time_to_seconds(time_str):
    minute, seconds = map(int, time_str.split(":"))
    return minute * 60 + seconds

def seconds_to_time(total_seconds):
    # 분과 초를 구하고, 두 자리 숫자로 맞춤 (01:05 등)
    m = total_seconds // 60
    s = total_seconds % 60
    return f"{m:02d}:{s:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    # 1. 모든 입력을 '초' 단위 숫자로 미리 변환합니다.
    curr = time_to_seconds(pos)
    v_len = time_to_seconds(video_len)
    os = time_to_seconds(op_start)
    oe = time_to_seconds(op_end)

    # 2. 로직 수행 (시작 시점 체크 + 명령어 처리)
    # 명령어 처리 전후로 오프닝 구간인지 체크하는 함수
    def check_opening(time_pos):
        if os <= time_pos <= oe:
            return oe
        return time_pos

    # [시작 전 체크] 현재 위치가 오프닝 구간이면 건너뜀
    curr = check_opening(curr)

    for cmd in commands:
        if cmd == "prev":
            # 10초 전으로 이동 (0초보다 작아질 수 없음)
            curr = max(0, curr - 10)
        elif cmd == "next":
            # 10초 후로 이동 (영상 길이를 넘을 수 없음)
            curr = min(v_len, curr + 10)
        
        # [이동 후 체크] 이동한 위치가 오프닝 구간이면 건너뜀
        curr = check_opening(curr)

    # 3. 결과를 다시 mm:ss 형식으로 변환
    return seconds_to_time(curr)