class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #gta use backtracking
        res = []
        subset= []
        def dfs(i):
            #base case
            if i>=len(nums):
                res.append(subset.copy())
                return
            #no constraint here, so decision tree calls time
            subset.append(nums[i])
            dfs(i+1)
            #no element
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res    


        