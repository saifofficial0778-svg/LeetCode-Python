class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low,high=max(weights),sum(weights)

        while low<=high:
            mid=(low+high)//2

            day=1
            curr_sum=0
            for weight in weights:
                curr_sum+=weight
                if curr_sum>mid:
                    day+=1
                    curr_sum=weight

            if day<=days:
                high=mid-1
            else:
                low=mid+1
        return low
            


