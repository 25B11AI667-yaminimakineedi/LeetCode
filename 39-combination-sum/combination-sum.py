class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def sub(i,c,t,r=[],s=0):
            if s>t:
                return 
            if i>=len(c):
                if s==t:
                    ans.append(r.copy())
                return
            r.append(c[i])
            s+=c[i]
            sub(i,c,t,r,s)
            r.pop()
            s-=c[i]
            sub(i+1,c,t,r,s)
        sub(0,candidates,target)
        return ans