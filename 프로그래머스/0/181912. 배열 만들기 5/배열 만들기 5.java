import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        // 1. 조건을 만족하는 숫자를 담을 가변 리스트 생성
        List<Integer> list = new ArrayList<>();
        
        for (String str : intStrs) {
            // 2. s번 인덱스부터 l만큼 잘라내기
            // 예: s=5, l=5 라면 5번부터 10번 전까지(5, 6, 7, 8, 9) 가져옴
            String sub = str.substring(s, s + l);
            
            // 3. 숫자로 변환
            int num = Integer.parseInt(sub);
            
            // 4. k보다 큰 경우에만 리스트에 추가
            if (num > k) {
                list.add(num);
            }
        }
        
        // 5. 리스트를 int[] 배열로 변환
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}