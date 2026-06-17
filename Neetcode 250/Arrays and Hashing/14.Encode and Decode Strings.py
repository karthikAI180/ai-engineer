class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + '#' + i
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        ind = 0
        while ind < len(s):
            j = ind
            while s[j] != '#':
                j += 1
            val = int(s[ind:j])
            ind = j + 1
            decoded.append(s[ind:ind+val])
            ind += val
        return decoded
