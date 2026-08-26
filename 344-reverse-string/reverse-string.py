class Solution:
    def reverseString(self, s: List[str]) -> None:
        def rs(i,j,s):
            if(i>=j):
                print(s)
                return 
            s[i],s[j]=s[j],s[i]
            rs(i+1,j-1,s)
        rs(0,len(s)-1,s)
        
            