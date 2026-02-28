class Solution {
    public long maximumSubsequenceCount(String text, String pattern) {
        char a = pattern.charAt(0);
        char b = pattern.charAt(1);
        
        long countA = 0;
        long countB = 0;
        long subsequences = 0;
        
        for (char ch : text.toCharArray()) {
            if (ch == b) {
                subsequences += countA; 
                countB++;
            }
            if (ch == a) {
                countA++;
            }
        }
        
        return subsequences + Math.max(countA, countB);
    }
}