class Solution:
    def hasDuplicate(self, nums) -> bool:
        k=set()
        for i in nums:
            k.add(i)
        if len(k)!=len(nums):
            return True
        return False

        