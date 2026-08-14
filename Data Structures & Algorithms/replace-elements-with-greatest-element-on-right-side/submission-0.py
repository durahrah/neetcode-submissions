class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            max = 0
            for j in range(i+1,len(arr)):
                if(arr[j]>max):
                    max = arr[j]
            arr[i]=max
        arr[len(arr)-1]=-1
        return arr            

        