class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        hashh={}
        for i in range(len(pattern)):
            if pattern[i] in hashh:
                if hashh[pattern[i]]!=words[i]:
                    return False
            else:
                if words[i] in hashh.values():
                    return False
                hashh[pattern[i]]=words[i]
        return True
               

            