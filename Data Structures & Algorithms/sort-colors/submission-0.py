class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0,0,0]
        for i in nums:
            count[i]+=1
        i,j = 0,0    
        for c in count:
            while c>0:
                nums[i]=j
                i+=1
                c-=1
            j+=1    
        return nums        
        