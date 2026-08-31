class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       hashh={}
       for i in nums2:
            if i in hashh:
                hashh[i]+=1
            else:
                hashh[i]=1

       nums=[]
       for i in nums1:
            if i in hashh and hashh[i]>0:
                    nums.append(i)
                    hashh[i]-=1
       return nums