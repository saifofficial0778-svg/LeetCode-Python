class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)

        while low<high:
            k=(low+high)//2

            hours=0

            for pile in piles:
                hours+=(pile+k-1)//k

            if hours<=h:
                high=k
            else:
                low=k+1

        return low