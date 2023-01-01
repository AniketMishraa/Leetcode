class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp = []
        l,r = 0, len(nums) - 1 
        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                temp.append(nums[l] * nums[l])
                l+= 1
            else:
                temp.append(nums[r] * nums[r])
                r -= 1
            
            
        return temp[::-1]