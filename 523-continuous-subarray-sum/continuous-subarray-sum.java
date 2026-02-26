class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer,Integer> res=new HashMap<>();
        res.put(0,-1);
        int n=nums.length;
        int prefix=0;
        for(int i=0;i<n;i++){
            prefix+=nums[i];
        

        int rem=prefix%k;
        if(res.containsKey(rem)){
            if(i-res.get(rem)>=2){
                return true;
            }
        }else{
            res.put(rem,i);
        }
        }
        return false;


    }
}