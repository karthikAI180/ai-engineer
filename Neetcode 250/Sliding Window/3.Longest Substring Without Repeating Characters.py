class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        new=""
        res=0
        while l<len(s) and r<len(s):
            if s[r] not in new:
                r+=1
            else:
                l+=1
            new=s[l:r]
            print(new,l,r)
            res=max(res,len(new))
        return res


        