class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points,(a,b)->Integer.compare(a[0],b[0]));
        int arrows=1;
        int prevS=points[0][0];
        int prevE=points[0][1];
        for(int i=1;i<points.length;i++){
            int currS=points[i][0];
            int currE=points[i][1];
            if(currS>prevE){
                arrows++;
                prevS=currS;
                prevE=currE;
            }else{
                prevS=Math.max(prevS,currS);
                prevE=Math.min(prevE,currE);
            }
        }
        return arrows;
    }
}