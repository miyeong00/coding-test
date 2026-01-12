class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = 0;
        
        char[] code_lst = code.toCharArray();
        
        for (int i = 0; i < code_lst.length; i++) {
            if (mode == 0) {
                if (code_lst[i] != '1') {
                    if (i % 2 == 0) {
                        answer += code_lst[i];
                    }
                } else {
                    mode = 1;
                }
            } else {
                if (code_lst[i] != '1') {
                    if (i % 2 == 1) {
                        answer += code_lst[i];
                    }
                } else {
                    mode = 0;
                }
            }
        }
        
        if (answer.length() == 0) {
            return "EMPTY";
        } else {
            return answer;
        }
    }
}