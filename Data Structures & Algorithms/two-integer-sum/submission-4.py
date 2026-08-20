class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        count = {}
        i=0
        for n in nums:
            if target-n in count:
                return [count[target-n],i]
            if n not in count:
                count[n]=i    
            i+=1    
