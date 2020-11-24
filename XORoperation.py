
#xoroperation
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        a = 0
        for i in range(0,n):
            nums.append(start + 2 * i)
        for i in nums:
            a ^= i
        return a
            
            
        