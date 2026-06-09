class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in k:
                return [k[diff],i]
            k[nums[i]]=i
        return 
        