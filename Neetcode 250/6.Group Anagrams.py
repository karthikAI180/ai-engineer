class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)#mapping charCount to list of anagram
        for s in strs:
            count=[0]*26
            for i in s:
                count[ord(i)-ord('a')]+=1
            res[tuple(count)].append(s)
        print(res.values())
        return list(res.values())

