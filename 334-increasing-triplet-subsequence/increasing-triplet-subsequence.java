class Solution {
    public boolean increasingTriplet(int[] nums) {
        int i=Integer.MAX_VALUE,j=Integer.MAX_VALUE;
        for(int l=0;l<nums.length;l++){
            if(nums[l]<=i){
                i=nums[l];
            }else if(nums[l]<=j){
                j=nums[l];
            }else {
                return true;
            }
        }
        return false;
    }
}