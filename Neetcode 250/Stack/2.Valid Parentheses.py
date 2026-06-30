class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        matches={'}':'{',']':'[',')':'('}
        for i in s:
            if i in '{[(':
                stack.append(i)
            else:
                if not stack or (stack[-1]!=matches.get(i)):
                    return False
                else:
                    stack.pop()
        return len(stack)==0
            


        