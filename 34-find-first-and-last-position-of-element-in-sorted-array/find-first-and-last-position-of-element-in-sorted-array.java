public class Solution {
    private int findLeft(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        int result = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] >= target) {
                if (nums[mid] == target) {
                    result = mid;  
                }
                high = mid - 1;  
            } else {
                low = mid + 1;  
            }
        }
        return result;
    }
    
    
    private int findRight(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        int result = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] <= target) {
                if (nums[mid] == target) {
                    result = mid;  
                }
                low = mid + 1;  
            } else {
                high = mid - 1;  
            }
        }
        return result;
    }
    
    public int[] searchRange(int[] nums, int target) {
        int left = findLeft(nums, target);
        int right = findRight(nums, target);
        return new int[]{left, right};
    }
}