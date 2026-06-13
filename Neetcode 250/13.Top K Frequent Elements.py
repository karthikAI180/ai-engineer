class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums) + 1)]
        h={}
        res=[]
        for i in nums:
            h[i]=h.get(i,0)+1
        for a,b in h.items():
            count[b].append(a)
        for i in range(len(count)-1,0,-1):
            for j in range(len(count[i])):
                if k>0:
                    res.append(count[i][j])
                    k-=1
        
        return res
        