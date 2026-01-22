import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> stk = new ArrayList<>();
        int i = 0;
        
        // i가 배열 끝에 도달할 때까지 반복
        while (i < arr.length) {
            if (stk.isEmpty()) { // 1. stk가 비었을 때
                stk.add(arr[i]);
                i++;
            } else {
                // 2. stk의 마지막 원소 가져오기
                int lastValue = stk.get(stk.size() - 1);
                
                if (lastValue < arr[i]) {
                    stk.add(arr[i]);
                    i++;
                } else {
                    // 3. stk의 마지막 원소가 arr[i]보다 크거나 같으면 삭제
                    // 이때 i는 증가시키지 않고 다음 루프에서 다시 검사합니다!
                    stk.remove(stk.size() - 1);
                }
            }
        }
        
        // 4. List를 int[]로 변환
        int[] answer = new int[stk.size()];
        for (int j = 0; j < stk.size(); j++) {
            answer[j] = stk.get(j);
        }
        
        return answer;
    }
}