class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        int n=words.length;
        int[] pre=new int[n];
        for(int i=0;i<n;i++){
            String word=words[i];
            if (isvowel(word.charAt(0))&&isvowel(word.charAt(word.length()-1))){
                pre[i]=1;

            }
            if(i>0){
                pre[i]+=pre[i-1];
            }
        }
        int[] res=new int[queries.length];
        for(int i=0;i<queries.length;i++){
            int l=queries[i][0];
            int r=queries[i][1];
            if(l==0){
                res[i]=pre[r];
            }else{
                res[i]=pre[r]-pre[l-1];
            }
        }
        return res;

    }
    private boolean isvowel(char ch){
        return ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u';
    }
}