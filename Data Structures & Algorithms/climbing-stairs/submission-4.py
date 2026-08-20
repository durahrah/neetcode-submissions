class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1,1
        #we are solving using dynamic programming approach
        #bottom up dp approach
        for i in range(n-1):
            temp = one
            one= one+two
            two = temp 
        return one    

       