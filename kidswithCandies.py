#kidswithCandies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = max(candies)
        b = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= a:
                print(candies[i])
                b.append(True)
            else:
                b.append(False)
                
        print(b)
        return b
    
        