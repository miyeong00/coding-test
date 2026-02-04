class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        StringBuilder sb = new StringBuilder();
        
        // my_strings.size() -> my_strings.length 로 수정
        for (int i = 0; i < my_strings.length; i++) {
            int s = parts[i][0];
            int e = parts[i][1];
            
            // i번째 문자열에서 s부터 e까지 잘라서 붙이기
            sb.append(my_strings[i].substring(s, e + 1));
        }
        
        return sb.toString();
    }
}