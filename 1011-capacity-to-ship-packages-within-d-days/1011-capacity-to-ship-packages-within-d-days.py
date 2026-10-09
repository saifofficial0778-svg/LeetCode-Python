class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low,high=max(weights),sum(weights)

        while low<=high:
            mid=(low+high)//2

            count=1
            curr_w=0
            for w in weights:
                curr_w+=w

                if curr_w>mid:
                    count+=1
                    curr_w=w
            if count<=days:
                high=mid-1
            else:
                low=mid+1
        return low