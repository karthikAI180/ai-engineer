class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(31,-1,-1):
            k=n&1
            res|=k<<i
            n=n>>1
        return res

        