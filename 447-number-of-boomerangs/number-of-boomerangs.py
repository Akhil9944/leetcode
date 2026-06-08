from collections import defaultdict
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0

        for x1, y1 in points:
            dist_count = defaultdict(int)

            for x2, y2 in points:
                dx = x1 - x2
                dy = y1 - y2
                dist = dx * dx + dy * dy

                dist_count[dist] += 1

            for count in dist_count.values():
                ans += count * (count - 1)

        return ans