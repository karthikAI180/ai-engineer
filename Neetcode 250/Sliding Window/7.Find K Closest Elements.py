class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        for r in range(k,len(arr)):
            if abs(arr[l] - x) < abs(arr[r] - x) or (abs(arr[l] - x) == abs(arr[r] - x) and arr[l]<arr[r]):
                return arr[l:r]
            l+=1
        return arr[l:]
        