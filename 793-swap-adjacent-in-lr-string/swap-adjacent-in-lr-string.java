class Solution {
    public boolean canTransform(String start, String result) {

        int n = start.length();

        int i = 0;
        int j = 0;

        while (i < n || j < n) {

            // skip X in start
            while (i < n && start.charAt(i) == 'X') {
                i++;
            }

            // skip X in result
            while (j < n && result.charAt(j) == 'X') {
                j++;
            }

            // both finished
            if (i == n && j == n) {
                return true;
            }

            // one finished earlier
            if (i == n || j == n) {
                return false;
            }

            char c1 = start.charAt(i);
            char c2 = result.charAt(j);

            // characters must match
            if (c1 != c2) {
                return false;
            }

            // L cannot move right
            if (c1 == 'L' && i < j) {
                return false;
            }

            // R cannot move left
            if (c1 == 'R' && i > j) {
                return false;
            }

            i++;
            j++;
        }

        return true;
    }
}