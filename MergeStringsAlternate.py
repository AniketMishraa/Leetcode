class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        temp = ""
        fl = 0
        if len(word1) < len(word2):
            t = len(word1)
            fl = 1
        else:
            t = len(word2)
            fl = 2
        for i in range(t):
            temp += word1[i]
            temp += word2[i]
        if fl == 1:
            temp += word2[t:]
        else:
            temp += word1[t:]
        return temp