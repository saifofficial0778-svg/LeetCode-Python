class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n=len(candies)

        if sum(candies)<k:
            return 0
        ans=0

        low,high=1,max(candies)

        while low<=high:
            candy=(low+high)//2

            count=0
            for pile in candies:
                count+=pile//candy

            if count>=k:
                ans=candy
                low=candy+1
            else:
                high=candy-1
        return ans


            
            









