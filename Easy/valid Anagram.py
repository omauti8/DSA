class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count1= {}
        count2={}
        for ch in s:
            count1[ch]= count1.get(ch,0)+1

        for ch in t:
             count2[ch]= count2.get(ch,0)+1
        
        return count1==count2