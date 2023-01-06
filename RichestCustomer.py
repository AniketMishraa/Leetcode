class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        temp = 0
        for i in accounts:
            temp = max(temp, sum(i))
        return temp