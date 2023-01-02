class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp = []
        for i in s:
            temp.append(i)
        if len(temp) == 0:
            return True
        if len(s) > len(t):
            return False
        for i in range(len(t)):
            if t[i] == temp[0]:
                temp.pop(0)
            if len(temp) == 0:
                return True
        return False