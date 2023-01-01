class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add = 0
        mul = 1
        for i in str(n):
            add += int(i)
            mul *= int(i)
        return mul - add