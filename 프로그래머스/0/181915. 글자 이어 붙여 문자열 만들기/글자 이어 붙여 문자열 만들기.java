class Solution {
    public String solution(String my_string, int[] index_list) {
        String answer = "";
        
        char[] charArr = my_string.toCharArray();
        StringBuilder sb = new StringBuilder();
        for (int idx : index_list) {
            sb.append(charArr[idx]);
        }
        
        return sb.toString();
    }
}