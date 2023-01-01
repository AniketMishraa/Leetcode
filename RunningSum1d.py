class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r = len(nums) - 1
        l = r - 1
        fin = []
        temp = 0
        if len(nums) == 1:
            return nums
        for i in range(len(nums)):
            while r >= 0:
                temp += nums[r]
                r -= 1
            fin.append(temp)
            temp = 0
            r = l
            l -= 1
        return fin[::-1]
            