class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low,high=1,m*n

        while low<=high:
            mid=(low+high)//2

            count=0
            
            for i in range(1,m+1):
                count+=min(mid//i,n)

            if count<k:
                low=mid+1
            else:
                high=mid-1
        return low
        