class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result=[]
        path=[]
        def ispalindrome(s,start,end):
            while start<=end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
        def func(s,ind,path,result):
            if ind==len(s):
                result.append(path.copy())
                return
            for i in range(ind,len(s)):
                if ispalindrome(s,ind,i):
                    path.append(s[ind:i+1])
                    func(s,i+1,path,result)
                    path.pop()
        func(s,0,path,result)
        return result

