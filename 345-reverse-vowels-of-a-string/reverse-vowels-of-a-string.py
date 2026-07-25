class Solution:
    def reverseVowels(self, s: str) -> str:
        
        def check(s,i,j):
            if(i<j):
                if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                    if s[j] in ['a','e','i','o','u','A','E','I','O','U']:
                        s[i],s[j]=s[j],s[i]
                        i+=1
                        j-=1
                        check(s,i,j)
                    else:
                        j-=1
                        check(s,i,j)
                else:
                    check(s,i+1,j)
        s=list(s)
        check(s,0,len(s)-1)    
        return "".join(s)