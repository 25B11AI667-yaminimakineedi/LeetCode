class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashh={}
        for i in range(len(s)):
            if s[i] in hashh:
                if hashh[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in hashh.values():
                    return False
                hashh[s[i]]=t[i]
        return True