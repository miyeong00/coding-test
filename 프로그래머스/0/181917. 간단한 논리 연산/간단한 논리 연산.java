class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        // 1. (x1 OR x2) 를 계산합니다.
        // 2. (x3 OR x4) 를 계산합니다.
        // 3. 두 결과를 AND 로 묶습니다.
        
        boolean answer = (x1 || x2) && (x3 || x4);
        
        return answer;
    }
}