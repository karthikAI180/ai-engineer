class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Method 1
        '''
        k={}
        res=0
        maxcount=0
        for i in nums:
            k[i]=k.get(i,0)+1
            res=i if k[i]>maxcount else res
            maxcount=max(k[i],maxcount)
        print(k)
         #USING DICT for k,v in k.items():
        #     if v>len(nums)/2:
        #         return k
        return res
        '''
        #Method 2
        count=1
        res=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==res:
                count+=1
            else:
                count-=1
            if count<0:
                res=nums[i]
        return res