class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ''' O(NLOGN)
        if len(nums)==0:
            return 0
        nums.sort()
        res=0
        curr=nums[0]
        streak=0 
        i=0
        while i<len(nums):
            if curr!=nums[i]:
                curr=nums[i]
                streak=0
            while i<len(nums) and nums[i]==curr:
                i+=1
            streak+=1
            curr+=1
            res=max(res,streak)
        return res
        '''
        k=set(nums)
        longest=0
        for n in k:
            if n-1 not in k:
                length=0
                while n+length in k:
                    length+=1
                longest=max(length,longest)
        return longest


        