class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=0
        b=0
        res=""
        while a<len(word1) and b<len(word2):
            res+=word1[a]+word2[b]
            a+=1
            b+=1
        while a<len(word1):
            res+=word1[a]
            a+=1
        while b<len(word2):
            res+=word2[b]
            b+=1
        return res