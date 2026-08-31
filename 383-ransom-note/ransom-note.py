class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_ransomnote={}
        hash_magazine={}
        for i in ransomNote:
            if i in hash_ransomnote :
                hash_ransomnote[i]+=1
            else:
                hash_ransomnote[i]=1
        for i in magazine:
            if i in hash_magazine:
                hash_magazine[i]+=1
            else:
                hash_magazine[i]=1
        for i in ransomNote:
            if i not in magazine:
                return False
            if hash_ransomnote[i]>hash_magazine[i]:
                return False
        return True



