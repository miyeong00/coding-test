class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        int[] arr = new int[included.length];
        
        for (int i=0; i<included.length; i++) {
            arr[i] = a;
            if (included[i] == true) {
                answer += arr[i];
            }
            a += d;
        }
        
        return answer;
    }
}