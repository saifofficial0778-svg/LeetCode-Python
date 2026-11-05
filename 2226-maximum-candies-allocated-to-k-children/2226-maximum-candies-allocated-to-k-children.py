class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if sum(candies)<k:
            return 0
        low,high=1,max(candies)
        n=len(candies)
        ans=0

        while low<=high:
            mid=(low+high)//2

            count=0

            for pile in candies:
                if pile>=mid:
                    count+=pile//mid
                    
            
            if count>=k:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans