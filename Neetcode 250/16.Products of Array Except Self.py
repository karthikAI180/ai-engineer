class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res=[0]*len(nums)
        prefix=1
        postfix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i]*= postfix
            postfix *= nums[i]
        return res

#0(n),0(n)-> time ans space
        # pre=[0]*(len(nums)+1)
        # post=[0]*(len(nums)+1)
        # res=[0]*len(nums)
        # pre[0]=1
        # post[len(post)-1]=1
        # for i in range(1,len(pre)):
        #     pre[i]=pre[i-1]*nums[i-1]
        # for j in range(len(post)-2,-1,-1):
        #     post[j]=post[j+1]*nums[j]
        # for i in range(len(pre)-1):
        #     res[i]=pre[i]*post[i+1]
        # return res
        