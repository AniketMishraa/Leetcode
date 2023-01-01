class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = len(nums) - 2, len(nums) - 1
        while l >= 0:
            if nums[l] == 0:
                temp = nums.pop(l)
                nums.append(0)
            l -= 1