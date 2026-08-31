class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashh={}
        for i in s:
            if i in hashh:
                hashh[i]+=1
            else:
                hashh[i]=1
        for i in range(len(s)):
            if hashh[s[i]]==1:
                return i
        return -1
        