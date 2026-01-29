class Solution {
    public int solution(String number) {
        int answer = 0;
        
        for(char n : number.toCharArray()) {
            answer += Character.getNumericValue(n);
        }
        
        answer %= 9;
        
        return answer;
    }
}