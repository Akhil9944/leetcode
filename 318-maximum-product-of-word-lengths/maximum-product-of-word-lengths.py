class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
       
        masks = {}
        
        for word in words:
            bitmask = 0
            for char in word:
                bitmask |= (1 << (ord(char) - ord('a')))
            
            masks[bitmask] = max(masks.get(bitmask, 0), len(word))
        
        max_prod = 0
        
        for mask1, len1 in masks.items():
            for mask2, len2 in masks.items():
                if (mask1 & mask2) == 0:
                    max_prod = max(max_prod, len1 * len2)
                    
        return max_prod