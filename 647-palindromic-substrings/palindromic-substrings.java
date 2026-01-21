class Solution {
    public int countSubstrings(String s) {
        int n=s.length();
        int count=0;
        for(int i=0;i<n;i++){
            count+=expandC(s,i,i);
            count+=expandC(s,i,i+1);
        }
        return count++;

    }
    private int expandC(String s,int left,int right){
        int cnt=0;
        while(left>=0&&right<s.length()&&s.charAt(left)==s.charAt(right)){
            cnt++;
            left--;
            right++;
        }
        return cnt;
    }
}