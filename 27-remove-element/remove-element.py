class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        x=[]
        for i in nums:
            if i!=val:
                count+=1
                x.append(i)
        nums[:]=x
       


                
        