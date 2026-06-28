class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        k=0
        while k<=n:
            i=k
            count=0
            while i:
                count+=1
                i=i&(i-1) 
            k+=1
            res.append(count)
        return res

        