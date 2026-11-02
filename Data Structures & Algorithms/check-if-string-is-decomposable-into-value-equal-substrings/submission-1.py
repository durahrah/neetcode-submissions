class Solution:
    def isDecomposable(self, s: str) -> bool:
        pairs = 0
        i = 0
        while i < len(s):
            j = i+1
            while j < len(s) and s[j] == s[i]:
                j += 1
            remainder = (j-i)%3
            if remainder == 1:
                return False
            if remainder == 2:
                pairs += 1
            i = j
        return pairs == 1
