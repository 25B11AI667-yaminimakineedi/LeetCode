class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        for i in accounts:
            sum_amount=0
            for j in i:
                sum_amount+=j
            max_wealth=max(max_wealth,sum_amount)
        return max_wealth
