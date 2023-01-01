class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0, len(nums) - 1
        if k == 0:
            return nums
        while k > 0:
            temp = nums.pop()
            nums.insert(0,temp)
            l += 1
            r -= 1
            k -= 1