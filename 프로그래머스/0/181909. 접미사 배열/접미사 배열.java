import java.util.Arrays;

class Solution {
    public String[] solution(String my_string) {
        int n = my_string.length();
        // 1. 접미사들을 담을 배열을 만듭니다. (길이는 문자열의 길이와 같아요)
        String[] answer = new String[n];
        
        // 2. 반복문을 돌며 각 위치에서 시작하는 접미사를 추출합니다.
        for (int i = 0; i < n; i++) {
            // substring(i)는 i번 인덱스부터 끝까지 잘라줍니다.
            answer[i] = my_string.substring(i);
        }
        
        // 3. 자바의 Arrays.sort()를 사용해 사전순(오름차순)으로 정렬합니다.
        Arrays.sort(answer);
        
        return answer;
    }
}