class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        if nums[mid] > target:
            for i in range(mid):
                if nums[i] == target:
                    return i
        else:
            for i in range(mid,len(nums)):
                if nums[i] == target:
                    return i

        return -1