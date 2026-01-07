class Solution {
    public int solution(int a, int b) {
        int num1 = Integer.parseInt(a + "" + b);
        int num2 = 2 * a * b;
        
        if (num1 >= num2) {
            return num1;
        } else {
            return num2;
        }
    }
}