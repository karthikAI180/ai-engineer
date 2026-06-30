class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        cur=''
        num=0
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i=='[':
                stack.append((cur,num))
                cur=''
                num=0
            elif i==']':
                prev,fact=stack.pop()
                cur=prev+cur*fact
            else:
                cur+=i
        return cur
