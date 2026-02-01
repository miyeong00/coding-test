class Solution {
    public String solution(String my_string, int[][] queries) {
        // 1. 수정을 위해 문자열을 문자 배열로 변환합니다.
        char[] arr = my_string.toCharArray();
        
        // 2. 여러 번의 쿼리를 수행합니다.
        for (int[] query : queries) {
            int s = query[0];
            int e = query[1];
            
            // 3. s부터 e까지의 구간을 뒤집습니다.
            // 양 끝에서 시작하여 가운데로 오면서 값을 맞바꿉니다.
            while (s < e) {
                char temp = arr[s];
                arr[s] = arr[e];
                arr[e] = temp;
                
                s++; // 시작 인덱스는 증가
                e--; // 끝 인덱스는 감소
            }
        }
        
        // 4. 조작이 끝난 문자 배열을 다시 문자열로 만들어 반환합니다.
        return new String(arr);
    }
}