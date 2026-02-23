class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = set()

        for i in range(len(s) - k + 1):
            tmp = s[i:i+k]
            got.add(tmp)
            if len(got) == need:
                return True
                
        return len(got) == need