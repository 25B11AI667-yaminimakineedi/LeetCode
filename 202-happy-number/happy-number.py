class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        while n!=1:
            if n in visited:
                return False
            visited.add(n)
            sq=0
            while n>0:
                digit=n%10
                sq+=digit*digit
                n//=10
            n=sq
        return True        
       
