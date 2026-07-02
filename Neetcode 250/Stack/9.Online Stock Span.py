class StockSpanner:

    def __init__(self):
        self.stack=[] # pair: (price, span)
        

    def next(self, price: int) -> int:
        count=1
        while self.stack and self.stack[-1][0]<=price:
            count+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,count))
        return count
        # for i in range(len(self.stack)-1,-1,-1):
        #     if self.stack[i]<=price:
        #         count+=1
        #     else:
        #         self.stack.append(price)
        #         return count
        # self.stack.append(price)
        # return count



        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)