class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        num1 = num2 = -1
        cnt1 = cnt2 = 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 = 1
                num1 = num
            elif cnt2 == 0:
                cnt2 = 1
                num2 = num
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1

        res = []
        if cnt1 > n // 3:
            res.append(num1)
        if cnt2 > n // 3:
            res.append(num2)

        return res
        '''
        ele1=None
        ele2=None
        count1=0
        count2=0
        res=[]
        for i in range(len(nums)):
            if ele1 is None  or ele1==nums[i]:
                count1+=1
                ele1=nums[i]
            elif ele2 is None  or ele2==nums[i]:
                count2+=1
                ele2=nums[i]
            else:
                count1-=1
                count2-=1
                if count1==0:
                    ele1=None
                if count2==0:
                    ele2=None
        if nums.count(ele1) > len(nums) // 3:
            res.append(ele1)
        if nums.count(ele2) > len(nums) // 3:
            res.append(ele2)
        return res
        '''