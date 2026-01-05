class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String front = my_string.substring(0, s);
        
        // 자바에서는 끝 인덱스를 안 적으면 알아서 끝까지 자름.
        String back = my_string.substring(s + overwrite_string.length());
        
        return front + overwrite_string + back;
    }
}