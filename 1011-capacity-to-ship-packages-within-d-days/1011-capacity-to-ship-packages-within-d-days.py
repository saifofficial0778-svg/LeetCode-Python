class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        n=len(weights)
        low,high=max(weights),sum(weights)

        while low<high:
            day=(low+high)//2

            count=0
            curr_weight=0
            for weight in weights:
                curr_weight+=weight
                if curr_weight>day:
                    count+=1
                    curr_weight=weight
            count+=1
            if count<=days:
                high=day
            else:
                low=day+1
        return low

