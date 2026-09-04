class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def subset_sum(i,a,target,sum=0,r=[]):
            if sum>target:
                return
            if i >=len(a):
                if sum==target:
                    ans.append(r.copy())
                return
            r.append(a[i])
            sum+=a[i]
            subset_sum(i+1,a,target,sum,r)
            r.pop()
            sum-=a[i]
            j=i+1
            while j<len(a) and a[j]==a[i]:
                j+=1                    
            subset_sum(j,a,target,sum,r)
        subset_sum(0,candidates,target)
        return ans
        