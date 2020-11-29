#Remove Vowels

class Solution:
    def removeVowels(self, S: str) -> str:
        vowel = ['a','e','i','o','u']
        for i in vowel:
            S = S.replace(i,"")
        return S
        