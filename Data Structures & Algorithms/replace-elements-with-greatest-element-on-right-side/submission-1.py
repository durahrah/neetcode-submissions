class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #going from back to front
        #building up one by one
        #the very first max is -1/0 we dc
        #new max = (old max, arr[i])
        oldMax = -1
        for i in range(len(arr)-1,-1,-1):
            #going from back to front
            newMax = max(oldMax, arr[i])
            arr[i]=oldMax
            oldMax = newMax
        return arr    
