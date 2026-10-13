import heapq
import math

class Solution(object):
    def pickGifts(self, gifts, k):
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            reduced = int(math.sqrt(largest))
            heapq.heappush(max_heap, -reduced)
            
        return -sum(max_heap)