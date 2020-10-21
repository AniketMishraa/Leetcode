
#Add Binary


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        Aint = int(a,2)
        Bint = int(b,2)
        Abin = bin(Aint)
        Bbin = bin(Bint)
        integer_sum = int(Abin, 2) + int(Bbin, 2)
        final = bin(integer_sum)
        final1 = final[2:]
        return final1