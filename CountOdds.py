class Solution:
    def countOdds(self, low: int, high: int) -> int:
        #fin = 0
        #while low < high:
        #    if low % 2 != 0:
        #        fin += 1
        #    low += 1
        #if high % 2 != 0:
        #    fin += 1
        #return fin
        if low % 2 == 0 and high % 2 == 0:
            return (((high - low) // 2))
        else:
            return (((high - low) // 2) + 1)