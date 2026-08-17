class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p)>len(s):
            return []
        p_count={}
        window_cnt={}

        for ch in p:
            p_count[ch]=p_count.get(ch,0)+1
        result=[]
        left=0
        for right in range(len(s)):
            window_cnt[s[right]]=window_cnt.get(s[right],0)+1
            if right -left+1>len(p):
                window_cnt[s[left]]-=1
                if window_cnt[s[left]]==0:
                    del window_cnt[s[left]]
                left+=1
            if window_cnt==p_count:
                result.append(left)
        return result