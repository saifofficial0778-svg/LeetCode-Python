class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n=len(matrix[0])
        low,high=0,(len(matrix)*n)-1

        while low<=high:
            guess=(low+high)//2
            
            row=guess//n
            col=guess%n

            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                high=guess-1
            else:
                low=guess+1
            
        return False