class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        maxC = 0
        for i in range(len(nums)):
            if (nums[i]==1):
                c+=1
            else:
                if (maxC<c):
                    maxC = c
                c = 0
        if maxC<c:
            maxC = c        
        return maxC                
        