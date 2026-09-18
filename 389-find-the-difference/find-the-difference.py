class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s=Counter(s)
        count_t=Counter(t)
        for i in t:
            if count_t[i]>count_s[i]:
                return i
            
            