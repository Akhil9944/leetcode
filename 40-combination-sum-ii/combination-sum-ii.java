import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);  
        List<List<Integer>> result = new ArrayList<>();
        backtrack(candidates, target, 0, 0, new ArrayList<>(), result);
        return result;
    }
    
    private void backtrack(int[] candidates, int target, int start, int currentSum, List<Integer> path, List<List<Integer>> result) {
        if (currentSum == target) {
            result.add(new ArrayList<>(path));  
            return;
        }
        if (currentSum > target) {
            return;
        }
        
        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }
            path.add(candidates[i]);
            backtrack(candidates, target, i + 1, currentSum + candidates[i], path, result);
            path.remove(path.size() - 1);
        }
    }
}
