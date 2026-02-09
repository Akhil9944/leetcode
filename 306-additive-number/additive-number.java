import java.math.BigInteger;

class Solution {
    public boolean isAdditiveNumber(String num) {
        int n = num.length();

        for (int i = 1; i <= n / 2; i++) {
            // first number leading zero check
            if (num.charAt(0) == '0' && i > 1) break;

            BigInteger first = new BigInteger(num.substring(0, i));

            for (int j = i + 1; j < n; j++) {
                // second number leading zero check
                if (num.charAt(i) == '0' && j - i > 1) break;

                BigInteger second = new BigInteger(num.substring(i, j));

                BigInteger a = first;
                BigInteger b = second;
                int k = j;

                while (k < n) {
                    BigInteger sum = a.add(b);
                    String s = sum.toString();

                    if (!num.startsWith(s, k)) break;

                    k += s.length();
                    a = b;
                    b = sum;
                }

                if (k == n) return true;
            }
        }
        return false;
    }
}

