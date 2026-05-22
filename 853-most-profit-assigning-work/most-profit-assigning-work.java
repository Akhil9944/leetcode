class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {

        int n = difficulty.length;

        // Create jobs array
        int[][] jobs = new int[n][2];

        for (int i = 0; i < n; i++) {
            jobs[i][0] = difficulty[i];
            jobs[i][1] = profit[i];
        }

        // Sort jobs by difficulty
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);

        // Sort workers
        Arrays.sort(worker);

        int totalProfit = 0;

        int i = 0;
        int bestProfit = 0;

        // Process each worker
        for (int ability : worker) {

            // Move while worker can do the job
            while (i < n && jobs[i][0] <= ability) {

                bestProfit = Math.max(bestProfit, jobs[i][1]);

                i++;
            }

            totalProfit += bestProfit;
        }

        return totalProfit;
    }
}