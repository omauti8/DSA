class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict={}
        l=0
        max_len=0

        for r,ch in enumerate(s):
            if ch in dict and dict[ch]>=l:
                l= dict[ch]+1
            dict[ch]= r
            max_len= max(max_len, r-l+1)
        
        return max_len