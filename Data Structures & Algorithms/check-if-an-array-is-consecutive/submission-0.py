class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        freq = {}
        min = 100001
        max = 0
        for num in nums: #O(n)
            if num in freq:
                return False
            else:
                freq[num] = 1
                if num<min:#finds min
                    min = num
                if num>max: #finds max
                    max = num
        if max - min == len(nums) - 1:
            return True
        else:
            return False    


