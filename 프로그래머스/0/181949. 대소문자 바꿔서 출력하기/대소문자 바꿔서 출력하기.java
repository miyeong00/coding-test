import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String answer = "";
        
        for (int i = 0; i < a.length(); i++) {
            char c = a.charAt(i); // 문자열에서 i번째 문자를 가져옴.
            
            if (Character.isUpperCase(c)) {
                answer += Character.toLowerCase(c); // 대문자를 소문자로 바꿈
            } else {
                answer += Character.toUpperCase(c); // 소문자를 대문자로 바꿈 
            }
        }
        
        System.out.print(answer);
    }
}