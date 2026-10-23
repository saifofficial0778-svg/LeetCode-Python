class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if n<m*k:
            return -1
        low,high=1,max(bloomDay)

        while low<=high:
            mid=(low+high)//2

            f=0
            b=0

            for bloom in bloomDay:
                if bloom<=mid:
                    f+=1
                    if f==k:
                        b+=1
                        f=0
                else:
                    f=0
                
            if b>=m:
                high=mid-1
            else:
                low=mid+1
        return low