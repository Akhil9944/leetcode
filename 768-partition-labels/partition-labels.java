class Solution {
    public List<Integer> partitionLabels(String s) {
        int[] last=new int[26];
        for(int i=0;i<s.length();i++){
            last[s.charAt(i)-'a']=i;
        }
        List<Integer> ans=new ArrayList<>();

        int st=0;
        int ed=0;
        for(int i=0;i<s.length();i++){
            ed=Math.max(ed,last[s.charAt(i)-'a']);

            if(i==ed){
                ans.add(ed-st+1);
                st=i+1;

            }
        }
        return ans;
    }
}