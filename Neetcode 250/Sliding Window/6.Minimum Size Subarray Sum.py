class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size=len(nums)+1
        sum=0
        l=0
        r=0
        while r<len(nums):
            size=0
            sum+=nums[r]
            while sum>=target:
                size=r-l+1
                sum-=nums[l]
                l+=1
                min_size=min(min_size,size)
            r+=1
        if min_size==len(nums)+1:
            return 0
        return min_size
            
        