class Solution {
    public int maxArea(int[] height) {
        int left=0;
        int right=height.length-1;
        int maxw=0;
        while(left<right){
            int width=right-left;
            int h=Math.min(height[left],height[right]);
            int currentW=width*h;
            maxw=Math.max(maxw,currentW);
            if(height[left]<height[right]){
                left++;

            }else{
                right--;
            }
        }
        return maxw;
    }
}