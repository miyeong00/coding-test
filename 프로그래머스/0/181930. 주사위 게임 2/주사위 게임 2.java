class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        int plus = a + b + c;
        int db = (a*a) + (b*b) + (c*c);
        int triple = (a*a*a) + (b*b*b) + (c*c*c);
        
        if (a == b && b == c) {
            answer = plus * db * triple;
        } else if (a != b && b != c && a != c) {
            answer = plus;
        } else {
            answer = plus * db;
        }
        
        return answer;
    }
}