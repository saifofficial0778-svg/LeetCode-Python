class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        low1, high1=0,len(matrix)-1
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
        
        low2,high2=0,len(matrix[0])-1
        
        while low2<=high2:
            guess=(low2+high2)//2

            if matrix[row][guess]==target:
                return True
            elif matrix[row][guess]>target:
                high2=guess-1
            else:
                low2=guess+1
        return False
