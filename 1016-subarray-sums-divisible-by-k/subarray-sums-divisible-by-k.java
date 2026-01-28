class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        HashMap<Integer,Integer>map=new HashMap<>();
        map.put(0,1);
        int pre=0;
        int cnt=0;
        for(int num:nums){
            pre+=num;

            int rem=pre%k;
            if(rem<0){
                rem+=k;
            }
            if(map.containsKey(rem)){
                cnt+=map.get(rem);
            }
            map.put(rem,map.getOrDefault(rem,0)+1);
        }
     return cnt;
    }
}