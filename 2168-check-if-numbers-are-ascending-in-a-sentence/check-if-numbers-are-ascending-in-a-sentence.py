class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums=[]
        for value in s.split():
            if value.isdigit():
                nums.append(int(value))
        return all(nums[i]<nums[i+1] for i in range(len(nums)-1))
 