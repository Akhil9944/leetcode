class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {

        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> Double.compare(
                (double)arr[a[0]] / arr[a[1]],
                (double)arr[b[0]] / arr[b[1]]
            )
        );

        int n = arr.length;

        for (int j = 1; j < n; j++) {
            pq.offer(new int[]{0, j});
        }

        for (int count = 1; count < k; count++) {

            int[] cur = pq.poll();

            int i = cur[0];
            int j = cur[1];

            if (i + 1 < j) {
                pq.offer(new int[]{i + 1, j});
            }
        }

        int[] ans = pq.poll();

        return new int[]{
            arr[ans[0]],
            arr[ans[1]]
        };
    }
}