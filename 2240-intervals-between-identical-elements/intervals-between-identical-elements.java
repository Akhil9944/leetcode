class Solution {
    public long[] getDistances(int[] arr) {
        int n=arr.length;
        long[] res=new long[n];
        HashMap<Integer,List<Integer>> map=new HashMap<>();
        for(int i=0;i<n;i++){
            map.computeIfAbsent(arr[i],k->new ArrayList<>()).add(i);
        }
        for(List<Integer>indices:map.values()){
            int size=indices.size();
            long totsum=0;
            for(int ind:indices){
                totsum+=ind;
            }
            long prefixSum=0;
            for(int k=0;k<size;k++){
                int Curr=indices.get(k);

                long left=k;
                long right=size-k-1;
                long leftp=left*Curr-prefixSum;
                long rightp=(totsum-prefixSum-Curr)-right*Curr;
                res[Curr]=leftp+rightp;
                prefixSum+=Curr;

            }

        }
        return res;

    }
}