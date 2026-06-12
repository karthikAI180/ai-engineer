class Solution:
    def merge(self,nums,L,M,R):
        left=nums[L:M+1]
        right=nums[M+1:R+1]
        i=L
        j=0
        k=0
        while j<len(left) and k<len(right):
            if left[j]>right[k]:
                nums[i]=right[k]
                k+=1
            else:
                nums[i]=left[j]
                j+=1
            i+=1
        while j<len(left):
            nums[i]=left[j]
            j+=1
            i+=1
        while k<len(right):
            nums[i]=right[k]
            k+=1
            i+=1

    def mergeSort(self,nums,l,r):
        if l>=r:
            return
        m=(l+r)//2
        self.mergeSort(nums,l,m)
        self.mergeSort(nums,m+1,r)
        self.merge(nums,l,m,r)
        return nums
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums,0,len(nums))

        