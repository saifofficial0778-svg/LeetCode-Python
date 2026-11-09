class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low, high=1,m*n

        while low<=high:
            guess=(low+high)//2

            count=0

            for i in range(1,m+1):
                count+=min(guess//i,n)

            if count<k:
                low=guess+1
            else:
                high=guess-1
        return low