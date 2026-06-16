class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h=defaultdict(set)
        res=0
        sum=0
        h = { 0 : 1 }
        for i in nums:
            sum+=i
            if sum-k in h:
                res+=h[sum-k]
            h[sum]=h.get(sum,0)+1
        return res

          


        