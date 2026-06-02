class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        
        count = [0] * 101
        for num in arr:
            count[num] += 1
        
        ans = 0
        
        for x in range(101):
            for y in range(x, 101):
                z = target - x - y
                
                if z < y or z > 100:
                    continue
                
                # Case 1: x == y == z
                if x == y == z:
                    ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                
                # Case 2: x == y != z
                elif x == y:
                    ans += count[x] * (count[x] - 1) // 2 * count[z]
                
                # Case 3: x != y == z
                elif y == z:
                    ans += count[x] * count[y] * (count[y] - 1) // 2
                
                # Case 4: x < y < z
                else:
                    ans += count[x] * count[y] * count[z]
        
        return ans % MOD