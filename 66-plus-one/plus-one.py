class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        x=[]
        for i in digits:
            n=n*10+i
        n=n+1
        while n>0:
            a=n%10
            x.append(a)
            n=n//10
        return x[::-1]
