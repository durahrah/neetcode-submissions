class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x,y in points:
            d= x**2+y**2
            dist.append([d,[x,y]])
        #got euclidean 

        def QuickSort(arr:List[int], s:int, e:int)->List[int]:
            if e-s+1<=1: #base case
                return arr
            #choosing the right most val as index
            pivot = arr[e]
            ptr = s #index of starting element

            for i in range(s,e):
                if (arr[i][0]<pivot[0]):
                    #if small then swap w ptr element
                    temp=arr[i]
                    arr[i]=arr[ptr]
                    arr[ptr]=temp
                    ptr+=1
            #last swap w pivot and left ptr element
            arr[e]=arr[ptr]
            arr[ptr]=pivot

            #recursive call w left most array and right most array
            #we are sorting in place 
            QuickSort(arr, s, ptr-1)
            QuickSort(arr, ptr+1, e)

            return arr
        dist = QuickSort(dist, 0 , len(dist)-1)
        result = []
        for i in range(k):
            result.append(dist[i][1])
        return result




           


        