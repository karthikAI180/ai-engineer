class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=len(a)-1
        y=len(b)-1
        carry=0
        res=""
        while x >= 0 or y >= 0 or carry:
            bit_a = int(a[x]) if x >= 0 else 0
            bit_b = int(b[y]) if y >= 0 else 0
            total = bit_a + bit_b + carry
            res += str(total % 2)
            carry = total // 2
            x -= 1
            y -= 1
        # while x>=0 and y>=0:
        #     if carry+int(a[x])+int(b[y])==3:
        #         carry=1
        #         res+="1"
        #     elif carry+int(a[x])+int(b[y])==2:
        #         carry=1
        #         res+="0"
        #     elif carry+int(a[x])+int(b[y])==1:
        #         carry=0
        #         res+="1"
        #     else:
        #         carry=0
        #         res+="0"
        #     x-=1
        #     y-=1
        # while x>=0:
        #     if carry+int(a[x])==2:
        #         carry=1
        #         res+="0"
        #     elif carry+int(a[x])==1:
        #         carry=0
        #         res+="1"
        #     else:
        #         carry=0
        #         res+="0"
        #     x-=1
        # while y>=0:
        #     if carry+int(b[y])==2:
        #         carry=1
        #         res+="0"
        #     elif carry+int(b[y])==1:
        #         carry=0
        #         res+="1"
        #     else:
        #         carry=0
        #         res+="0"
        #     y-=1
        # if carry==1:
        #     res+='1'

        return res[::-1]

        