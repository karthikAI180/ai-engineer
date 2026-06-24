class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res=0
        freq={}
        max_freq=0
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
            max_freq=max(max_freq,freq[s[i]])
            if (i+1-l)-max_freq<=k:
                res = max(res, i - l + 1) 
            else:
                freq[s[l]]-=1
                l+=1
        return res




        