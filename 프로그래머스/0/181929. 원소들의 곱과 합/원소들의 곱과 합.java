class Solution {
    public int solution(int[] num_list) {
        int times = 1;
        int plus = 0;
        
        for (int num : num_list) {
            times *= num;
            plus += num;
        }
        if (times < plus * plus) {
            return 1;
        } else {
            return 0;
        }
    }
}