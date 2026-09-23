class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=""
        def ispalindrome(s,start,end):
            while start<=end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
        def func(s,index):
            nonlocal result
            if index==len(s):
                return
            for i in range(len(s)-1,index-1,-1):
               if ispalindrome(s,index,i):
                if len(s[index:i+1])>len(result):
                    result=s[index:i+1]
                break
            func(s,index+1)
        func(s,0)
        return result

        

