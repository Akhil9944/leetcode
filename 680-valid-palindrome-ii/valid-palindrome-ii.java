public class Solution {
    public boolean validPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        
        while (left < right) {
            if (s.charAt(left) == s.charAt(right)) {
                left++;
                right--;
            } else {
                // Check if skipping the left character makes it a palindrome
                if (isPalindrome(s, left + 1, right)) {
                    return true;
                }
                // Check if skipping the right character makes it a palindrome
                if (isPalindrome(s, left, right - 1)) {
                    return true;
                }
                return false;
            }
        }
        return true; // Already a palindrome
    }
    
    private boolean isPalindrome(String s, int start, int end) {
        while (start < end) {
            if (s.charAt(start) != s.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}
