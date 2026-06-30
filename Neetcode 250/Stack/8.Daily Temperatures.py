class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for i,c in enumerate(temperatures):
            while stack and c>temperatures[stack[-1]]:
                k=stack.pop()
                ans[k]=i-k
            stack.append(i)
        return ans
        