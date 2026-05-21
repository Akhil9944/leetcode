class Solution {
    public int numFriendRequests(int[] ages) {
      int[] count=new int[121];

      for(int age : ages){
        count[age]++;
      } 
      int ans=0;
      for(int ax=1;ax<=120;ax++){
        for(int ay=1;ay<=120;ay++){
            if(ay<=0.5*ax+7) continue;
            if(ay>ax) continue;
            if(ax==ay){
                ans+=count[ax]*(count[ax]-1);
            }else{
                ans+=count[ax]*count[ay];
            }
        }
      }
      return ans;
    }
}