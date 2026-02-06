class Solution {
    public int solution(String my_string, String is_suffix) {
        // endsWith() 결과가 true면 1, false면 0을 리턴합니다.
        return my_string.endsWith(is_suffix) ? 1 : 0;
    }
}