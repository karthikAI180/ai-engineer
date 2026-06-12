class ListNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class MyHashMap:

    def __init__(self):
        self.size=1000
        self.map=[ListNode(0,0)for i in range(self.size)]
        

    def put(self, key: int, value: int) -> None:
        cur=self.map[key%len(self.map)]
        while cur.next:
            if cur.next.key==key:
                if cur.next.value!=value:
                    cur.next.value=value
                return  
            cur=cur.next
        cur.next=ListNode(key,value)
    def get(self, key: int) -> int:
        cur=self.map[key%len(self.map)]
        while cur.next:
            if cur.next.key==key:
                return cur.next.value
            cur=cur.next
        return -1
    def remove(self, key: int) -> None:
        cur=self.map[key%len(self.map)]
        while cur.next:
            if cur.next.key==key:
                cur.next=cur.next.next
                return
        cur=cur.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)