import math

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        sum=0
        while n>0:
            x=n%10
            p=p*x
            sum=sum+x
            n=n//10
        return (p-sum)
