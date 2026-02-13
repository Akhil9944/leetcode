import java.util.*;

class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        
        if (digits == null || digits.length() == 0)
            return res;

        String[] map = {
            "",     // 0
            "",     // 1
            "abc",  // 2
            "def",  // 3
            "ghi",  // 4
            "jkl",  // 5
            "mno",  // 6
            "pqrs", // 7
            "tuv",  // 8
            "wxyz"  // 9
        };

        res.add("");

        for (char digit : digits.toCharArray()) {
            List<String> temp = new ArrayList<>();
            String letters = map[digit - '0'];

            for (String comb : res) {
                for (char letter : letters.toCharArray()) {
                    temp.add(comb + letter);
                }
            }

            res = temp;
        }

        return res;
    }
}