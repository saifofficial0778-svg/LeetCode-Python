class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n=len(matrix)
        low,high=matrix[0][0],matrix[n-1][n-1]

        while low<=high:
            mid=(low+high)//2

            row=n-1
            col=0
            count=0

            while row>=0 and col<n:
                if matrix[row][col]<=mid:
                    col+=1
                    count+=row+1
                else:
                    row-=1
            
            if count<k:
                low=mid+1
            else:
                high=mid-1
        return low

