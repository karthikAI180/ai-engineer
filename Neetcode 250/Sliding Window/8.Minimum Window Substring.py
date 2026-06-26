class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        l=0
        countT={}
        window={}
        for i in t:
            countT[i]=countT.get(i,0)+1
        have=0
        need=len(countT)
        res, resLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1
            if c in countT and window[c] == countT[c]:
                have += 1
            while need==have:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
                