class Solution {

    public int expressiveWords(String s, String[] words) {

        int count = 0;

        for(String word : words) {
            if(isStretchy(s, word)) {
                count++;
            }
        }

        return count;
    }

    private boolean isStretchy(String s, String word) {

        int i = 0;
        int j = 0;

        while(i < s.length() && j < word.length()) {

            // characters must match
            if(s.charAt(i) != word.charAt(j)) {
                return false;
            }

            char ch = s.charAt(i);

            int countS = 0;
            while(i < s.length() && s.charAt(i) == ch) {
                countS++;
                i++;
            }

            int countW = 0;
            while(j < word.length() && word.charAt(j) == ch) {
                countW++;
                j++;
            }

            // invalid conditions
            if(countS < countW) {
                return false;
            }

            if(countS != countW && countS < 3) {
                return false;
            }
        }

        return i == s.length() && j == word.length();
    }
}