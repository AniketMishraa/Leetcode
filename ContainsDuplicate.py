class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t = {}
        for i in nums:
            if i in t:
                return True
            t[i] = 0
        return False