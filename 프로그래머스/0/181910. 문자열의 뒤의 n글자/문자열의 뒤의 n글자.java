class Solution {
    public String solution(String my_string, int n) {
        // 1. 시작 위치 계산: 전체 길이에서 n을 뺍니다.
        int startIndex = my_string.length() - n;
        
        // 2. 그 위치부터 끝까지 잘라서 반환합니다.
        return my_string.substring(startIndex);
    }
}