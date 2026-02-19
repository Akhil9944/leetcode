class Solution {
    public int bestClosingTime(String customers) {
        int n = customers.length();
        
        int penalty = 0;
        
        // Step 1: Count total 'Y'
        for (char c : customers.toCharArray()) {
            if (c == 'Y') {
                penalty++;
            }
        }
        
        int minPenalty = penalty;
        int bestHour = 0;
        
        // Step 2: Move closing hour
        for (int i = 0; i < n; i++) {
            if (customers.charAt(i) == 'Y') {
                penalty--;   // removing future penalty
            } else {
                penalty++;   // adding open penalty
            }
            
            if (penalty < minPenalty) {
                minPenalty = penalty;
                bestHour = i + 1;
            }
        }
        
        return bestHour;
    }
}
