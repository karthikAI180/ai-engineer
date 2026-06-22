class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_min=nums[0]
        min_sum=nums[0]
        cur_max=nums[0]
        max_sum=nums[0]
        
        total=sum(nums)
        for i in nums[1:]:
            cur_max=max(cur_max+i,i)
            max_sum=max(max_sum,cur_max)
            cur_min=min(cur_min+i,i)
            min_sum=min(min_sum,cur_min)
        if max_sum<0:
            return max_sum
        return max(max_sum,total-min_sum)
        