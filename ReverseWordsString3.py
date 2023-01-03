class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ""
        l,r = 0,0
        print(len(s))
        while r < len(s):
            print(r)
            while s[r] != ' ':
                if r >= len(s)-1:
                    r += 1
                    break
                else:
                    r += 1
            t = s[l:r]
            t = t[::-1]
            temp += t
            if r >= len(s) - 1:
                pass
            else:
                temp += ' '
            r += 1
            l = r
        return temp