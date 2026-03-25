import re
import bisect

def solution(message, spoiler_ranges):
    # 1. 모든 단어 추출 (시작 인덱스, 끝 인덱스, 단어 문자열)
    # 단어는 알파벳 소문자와 숫자로만 구성됨
    words = []
    for m in re.finditer(r'[a-z0-9]+', message):
        words.append([m.start(), m.end() - 1, m.group()])
    
    if not words:
        return 0

    # 단어의 끝 인덱스만 모은 리스트
    word_ends = [w[1] for w in words]
    n = len(message)

    # 2. 모든 스포일러 구간 통합 표시 (is_spoiler_idx)
    # 차분 배열(Difference Array)을 사용해 효율적으로 계산
    is_spoiler_idx = [False] * n
    diff = [0] * (n + 1)
    for s, e in spoiler_ranges:
        diff[s] += 1
        diff[e + 1] -= 1
    
    curr = 0
    for i in range(n):
        curr += diff[i]
        if curr > 0:
            is_spoiler_idx[i] = True

    # 3. '일반 단어'로 등장한 적 있는 단어 세트 만들기
    # 단어의 모든 문자가 스포일러 구간에 속하지 않는 경우
    forbidden_strings = set()
    for start, end, w_str in words:
        is_word_spoiler = False
        for k in range(start, end + 1):
            if is_spoiler_idx[k]:
                is_word_spoiler = True
                break
        if not is_word_spoiler:
            forbidden_strings.add(w_str)

    # 4. 구간 클릭 시뮬레이션
    # 왼쪽부터 순서대로 클릭하므로 정렬
    spoiler_ranges.sort()
    
    processed_instances = set() # 이미 클릭되어 공개된 단어의 인덱스(위치 기준)
    revealed_strings = set()    # 이미 공개된 단어의 문자열 (중복 체크용)
    important_count = 0
    
    for s, e in spoiler_ranges:
        # 이진 탐색으로 현재 클릭 구간 [s, e]와 겹치는 첫 번째 단어 찾기
        start_idx = bisect.bisect_left(word_ends, s)
        
        current_click_indices = []
        for idx in range(start_idx, len(words)):
            w_start, w_end, w_str = words[idx]
            if w_start > e: # 구간을 벗어나면 중단
                break
            # 아직 공개되지 않은 단어 인스턴스라면 추가
            if idx not in processed_instances:
                current_click_indices.append(idx)
        
        # 여러 단어가 동시에 공개될 경우 왼쪽(인덱스 순)부터 판단
        for idx in current_click_indices:
            w_start, w_end, w_str = words[idx]
            
            # [중요한 단어 조건]
            # 1. 스포 방지 단어여야 함 (구간 내에 있으므로 당연히 충족)
            # 2. 일반 구간에 등장한 적 없어야 함 (forbidden_strings에 없어야 함)
            # 3. 이전에 공개된 스포 방지 단어와 중복되지 않아야 함
            if w_str not in forbidden_strings and w_str not in revealed_strings:
                important_count += 1
            
            # 조건 충족 여부와 상관없이 이 단어는 이제 '공개된 단어'임
            revealed_strings.add(w_str)
            processed_instances.add(idx)
            
    return important_count