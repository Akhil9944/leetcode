class Solution {
    public String removeKdigits(String num, int k) {
        if (k == num.length()) return "0";

        Deque<Character> stack = new ArrayDeque<>();

        for (char c : num.toCharArray()) {
            while (!stack.isEmpty() && k > 0 && stack.peekLast() > c) {
                stack.pollLast();
                k--;
            }
            stack.addLast(c);
        }

        while (k > 0) {
            stack.pollLast();
            k--;
        }

        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pollFirst());
        }

        int index = 0;
        while (index < sb.length() && sb.charAt(index) == '0') {
            index++;
        }

        String result = sb.substring(index);
        return result.isEmpty() ? "0" : result;
    }
}
