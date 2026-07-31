class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def mark_inf(matrix,row,col):
            r=len(matrix)
            c=len(matrix[0])

            for i in range(r):
                if matrix[i][col]!=0:
                    matrix[i][col]=float('inf')
            for j in range(c):
                if matrix[row][j]!=0:
                    matrix[row][j]=float('inf')
        r=len(matrix)
        c=len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    mark_inf(matrix,i,j)
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=0
                