import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int n = sc.nextInt();

        // 문자열.repeat(횟수) -> 파이썬의 * 연산과 동일!
        System.out.print(str.repeat(n));
    }
}