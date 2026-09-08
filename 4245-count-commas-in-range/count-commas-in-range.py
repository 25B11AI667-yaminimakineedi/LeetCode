class Solution:
    def countCommas(self, n: int) -> int:
        def num_commas(n):
            if n<=999:
               return 0
            digit_count=0
            comma_count=0
            while n>0:
                x=n%10
                digit_count+=1
                if digit_count==3:
                    comma_count+=1
                n=n//10
            return comma_count 
        count=0 
        for i in range(1000,n+1):
            x=num_commas(i)
            count+=x
        return count

