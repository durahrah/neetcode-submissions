class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res = r

        while l<=r:
            eats = (l+r)//2 #mid
            hours=0

            for p in piles:
                hours+=math.ceil(p/eats)

            if hours<=h:
                res = min(res,eats)
                r = eats - 1 #updating right so we can optimize
            else:
                l = eats + 1
        return res               

        

        

        