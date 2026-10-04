class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low,high=1,max(piles)
        while low<=high:
            k=(low+high)//2

            hour=0
            for pile in piles:
                hour+=(pile+k-1)//k
            if hour<=h:
                high=k-1
            else:
                low=k+1
        return low
