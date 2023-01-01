class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(len(nums))
        l,r = len(nums) - 1, len(nums) - 3
        print(nums[l:r])
        while r >= 0:
            if nums[r] + nums[r+1] > nums[l]:
                return nums[r] + nums[r+1] + nums[l]
            l -= 1
            r -= 1
        return 0

