class Solution:
    def myAtoi(self, s: str) -> int:
        sign=1
        i=0
        num=0
        x=s.strip()
        if not x:
            return 0
        if x[0]=="-":
            sign=-1
            i+=1
        if x[0]=="+":
            i+=1
        while i<len(x) and x[i].isdigit():
            num=num*10+int(x[i])
            i+=1
        num*=sign
        if num<-2**31:
            return -2**31
        if num>(2**31-1):
            return 2**31-1
        return num