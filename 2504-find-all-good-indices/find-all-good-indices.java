import java.util.*;

class Solution {
    public List<Integer> goodIndices(int[] nums, int k) {
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];
        
        // Step 1: Fill left array (non-increasing count)
        left[0] = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] <= nums[i - 1]) {
                left[i] = left[i - 1] + 1;
            } else {
                left[i] = 1;
            }
        }
        
        // Step 2: Fill right array (non-decreasing count)
        right[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] <= nums[i + 1]) {
                right[i] = right[i + 1] + 1;
            } else {
                right[i] = 1;
            }
        }
        
        // Step 3: Collect good indices
        List<Integer> result = new ArrayList<>();
        for (int i = k; i < n - k; i++) {
            if (left[i - 1] >= k && right[i + 1] >= k) {
                result.add(i);
            }
        }
        
        return result;
    }
}