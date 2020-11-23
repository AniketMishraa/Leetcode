#Running Sum

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = 0
        b= [] 
        for j in nums:   
            a = j+a
            b.append(a)
        return b