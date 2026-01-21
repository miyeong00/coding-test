import java.util.*;

class Solution {
    public int[] solution(int n) {
        // 1. 파이썬 리스트처럼 쓸 수 있는 ArrayList를 만듦.
        List<Integer> list = new ArrayList<>();
        
        // 2. 일단 시작 숫자 n을 넣음. (append 대신 add)
        list.add(n);
            
        while (n != 1) {
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = 3 * n + 1;
            }
            list.add(n);
        }
        
        // 3. ArrayList를 다시 int[]로 반환
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}