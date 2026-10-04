class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low,high=1,max(piles)
        while low<=high:
            mid=(low+high)//2

            hour=0
            for pile in piles:
                hour+=(pile+mid-1)//mid
            if hour<=h:
                high=mid-1
            else:
                low=mid+1
        return low
