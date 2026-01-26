import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> list = new ArrayList<>();
        
        for (int i = l; i <= r; i++) {
            String s = String.valueOf(i);
            boolean isZeroFive = true; // "이 숫자는 합격이야"라고 일단 깃발을 올림
            
            // 한 글자씩 검사하는 작은 반복문
            for (char c : s.toCharArray()) {
                if (c != '0' && c != '5') {
                    isZeroFive = false; // 0이나 5가 아닌 걸 발견하면 깃발을 내림
                    break; // 더 볼 것도 없으니 탈출!
                }
            }
            
            // 깃발이 여전히 올라가 있다면(true) 리스트에 추가
            if (isZeroFive) {
                list.add(i);
            }
        }
        
        // 결과 처리 (리스트가 비었으면 -1, 아니면 배열 변환)
        if (list.isEmpty()) return new int[]{-1};
        
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}