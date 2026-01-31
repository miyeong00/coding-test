import java.util.Arrays;

class Solution {
    public int solution(int a, int b, int c, int d) {
        // 1. 주사위 값을 배열에 넣고 오름차순으로 정렬합니다.
        int[] dice = {a, b, c, d};
        Arrays.sort(dice);
        
        // 정렬된 상태: dice[0] <= dice[1] <= dice[2] <= dice[3]
        
        // 케이스 1: 4개 숫자가 모두 같을 때
        if (dice[0] == dice[3]) {
            return 1111 * dice[0];
        }
        
        // 케이스 2: 3개 숫자가 같을 때
        else if (dice[0] == dice[2]) { // 앞의 3개가 같음 (예: 2 2 2 5)
            return (int) Math.pow(10 * dice[0] + dice[3], 2);
        }
        else if (dice[1] == dice[3]) { // 뒤의 3개가 같음 (예: 1 4 4 4)
            return (int) Math.pow(10 * dice[1] + dice[0], 2);
        }
        
        // 케이스 3: 2개씩 두 쌍이 같을 때 (예: 2 2 5 5)
        else if (dice[0] == dice[1] && dice[2] == dice[3]) {
            return (dice[0] + dice[2]) * Math.abs(dice[0] - dice[2]);
        }
        
        // 케이스 4: 2개만 같고 나머지 2개는 다를 때
        else if (dice[0] == dice[1]) { // 앞의 2개가 같음 (예: 2 2 3 5)
            return dice[2] * dice[3];
        }
        else if (dice[1] == dice[2]) { // 중간 2개가 같음 (예: 1 2 2 5)
            return dice[0] * dice[3];
        }
        else if (dice[2] == dice[3]) { // 뒤의 2개가 같음 (예: 1 3 5 5)
            return dice[0] * dice[1];
        }
        
        // 케이스 5: 4개 숫자가 모두 다를 때
        else {
            return dice[0]; // 정렬되었으므로 첫 번째 값이 가장 작음
        }
    }
}