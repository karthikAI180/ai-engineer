class Solution:
    '''
    Method 1 ->o(nklogk)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1 = sorted(s1)
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            window = s2[l:r+1]

            if sorted(window) == s1:
                return True

            l += 1
            r += 1

        return False
    '''

    '''
    Method 2 -> o(26n)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for ch in s1:
            count1[ord(ch) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            count2[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 > len(s1):
                count2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if count1 == count2:
                return True

        return False
    '''

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count1=[0]*26
        count2=[0]*26
        l=0
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')]+=1
            count2[ord(s2[i])-ord('a')]+=1
        matches=0
        for i in range(26):
            if count1[i]==count2[i]:
                matches+=1
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            i1=ord(s2[r])-ord('a')
            count2[i1]+=1
            if count2[i1]==count1[i1]:
                matches+=1
            elif count1[i1]+1==count2[i1]:
                matches-=1
            i2=ord(s2[l])-ord('a')
            count2[i2]-=1
            if count2[i2]==count1[i2]:
                matches+=1
            elif count1[i2]-1==count2[i2]:
                matches-=1
            l+=1
        return matches==26