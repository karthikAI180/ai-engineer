class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n:
            n=n&n-1
            count+=1
        return count
        # for i in range(32):
        #     if n&1==1:
        #         count+=1
        #     n=n>>1
        # return count
        