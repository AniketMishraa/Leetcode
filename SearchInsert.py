class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        if nums[mid] > target:
            for i in range(mid):
                if nums[i] == target:
                    return i
            for i in range(mid+1):
                print(i)
                print(nums[i])
                if nums[i] > target:
                    return i
            
            
        else:
            for i in range(mid, len(nums)):
                if nums[i] == target:
                    return i
            for i in range(mid, len(nums)):
                if nums[i] > target:
                    return i
        
        if nums[-1] < target:
            return len(nums)
        else:
            return len(nums) - 1