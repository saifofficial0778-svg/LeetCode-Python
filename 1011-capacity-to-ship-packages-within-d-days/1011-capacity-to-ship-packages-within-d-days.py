class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low,high=max(weights),sum(weights)

        while low<=high:
            mid=(low+high)//2

            count=1
            w_sum=0

            for weight in weights:
                w_sum+=weight
                if w_sum>mid:
                    count+=1
                    w_sum=weight
            if count<=days:
                high=mid-1
            else:
                low=mid+1
        return low
                