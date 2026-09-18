class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashh_s={}
        hashh_t={}
        for i in s:
            if i  in hashh_s:
                hashh_s[i]+=1
            else:
                hashh_s[i]=1
        for i in t:
            if i  in hashh_t:
                hashh_t[i]+=1
            else:
                hashh_t[i]=1
        for i in t:
            if hashh_t[i]>hashh_s.get(i,0):
                return i

            
            