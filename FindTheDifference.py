class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss,tt = 0,0
        for i in s:
            ss += ord(i)
        for i in t:
            tt += ord(i)
        fin = tt - ss
        return chr(fin)