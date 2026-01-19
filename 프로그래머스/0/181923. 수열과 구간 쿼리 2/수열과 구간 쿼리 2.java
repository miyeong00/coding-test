class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        // 1. 정답을 담을 배열을 쿼리 개수만큼 미리 만듭니다.
        int[] answer = new int[queries.length];
        int ansIdx = 0; // answer의 몇 번째 칸에 넣을지 결정하는 번호표
        
        // 2. 모든 쿼리를 하나씩 꺼내서 확인합니다.
        for (int[] query : queries) {
            int s = query[0];
            int e = query[1];
            int k = query[2];
            
            int min = 1000001;
            
            // 3. s부터 e까지 돌며 k보다 큰 최솟값 찾기
            for (int i = s; i <= e; i++) {
                if (arr[i] > k && arr[i] < min) {
                    min = arr[i];
                }
            }
            
            // 4. 결과값 담기 (append 대신 인덱스 사용!)
            if (min == 1000001) {
                answer[ansIdx] = -1;
            } else {
                answer[ansIdx] = min;
            }
            ansIdx++; // 다음 정답을 위해 번호표를 1 늘립니다.
        }
        
        return answer;
    }
}