class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=nums[0]
        res=nums[0]
        for i in nums[1:]:
            cur=max(cur+i,i)
            res=max(res,cur)
        return res
        # maxi=float('-inf')
        # sum=0
        # for i in nums:
        #     sum+=i
        #     maxi=max(maxi,sum)
        #     if sum<0:
        #         sum=0
        # return maxi