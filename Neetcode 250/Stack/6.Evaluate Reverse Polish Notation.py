class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=='+':
                res=stack[-2]+stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif i=='-':
                res=stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif i=='*':
                res=stack[-2]*stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif i=='/':
                res=int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[-1]
        