class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        temp = 99999
        a = 0
        for j,i in enumerate(points):
            if i[0] == x or i[1] == y:
                if ((abs(x - i[0]) + abs(y - i[1]))) < temp:
                    temp = (abs(x - i[0]) + abs(y - i[1]))
                    far = j
        
        
        if temp == 99999:
            return -1
        else:
            return far