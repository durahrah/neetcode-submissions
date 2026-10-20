class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #the three pointers
        i = m+n-1 #o/p pointer
        j = m-1 #nums1pointer
        k = n-1 #nums2 pointer
        while k>=0:
            if j>=0 and nums1[j]>=nums2[k]:
                temp = nums1[i]
                nums1[i]=nums1[j]
                nums1[j]= temp
                j-=1
            else:
                nums1[i]=nums2[k]
                k-=1        
            i-=1 #decrementing the o/p's pointer (since we are scainning back to front)