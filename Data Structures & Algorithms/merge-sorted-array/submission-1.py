class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #we will be looping till we reach both the end of nums1 and nums2
        p1 = m+n-1 #last
        i = m-1
        j = n-1
        while i>=0 and j>=0:
            if nums1[i]<nums2[j]:
                nums1[p1]=nums2[j]
                j-=1
                p1-=1
            else:
                nums1[p1]=nums1[i]
                i-=1
                p1-=1
        #filling the leftover num2
        while j>=0:
            nums1[p1]=nums2[j]
            j-=1
            p1-=1

        