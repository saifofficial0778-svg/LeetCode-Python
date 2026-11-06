class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        low1,high1=0,n-1
        row=-1

        while low1<=high1:
            guess=(low1+high1)//2

            if matrix[guess][0]<=target:
                row=guess
                low1=guess+1
            else:
                high1=guess-1
        if row==-1:
            return False

        low,high=0,m-1

        while low<=high:
            guess=(low+high)//2

            if matrix[row][guess]==target:
                return True
            elif matrix[row][guess]>target:
                high=guess-1
            else:
                low=guess+1
        return False
