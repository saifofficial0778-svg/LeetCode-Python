class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        low,high=1,max(bloomDay)

        while low<=high:
            day=(low+high)//2

            flowers=0
            bouquets=0

            for bloom in bloomDay:
                if bloom<=day:
                    flowers+=1
                    if flowers==k:
                        bouquets+=1
                        flowers=0
                else:
                    flowers=0
                
            if bouquets>=m:
                high=day-1
            else:
                low=day+1
        return low