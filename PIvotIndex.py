class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l,r = 0,len(nums)
        leftsum,rightsum = 0, sum(nums)
        a = 0
        for i in nums:
            rightsum -= i
            if rightsum == leftsum:
                return a
            leftsum += i
            a += 1
        return -1