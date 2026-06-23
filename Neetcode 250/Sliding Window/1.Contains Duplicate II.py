class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0:
            return False
        s=set()
        l=0
        s.add(nums[0])
        for r in range(1,len(nums)):
            if nums[r] in s:
                return True
            s.add(nums[r])
            if r-l>=k:
                s.remove(nums[l])
                l+=1
        return False
            

        