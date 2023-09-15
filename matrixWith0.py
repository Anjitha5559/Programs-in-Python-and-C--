class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        if m == 0:
            n = 0
        else:
            n = len(matrix[0])
            rows,cols = set(),set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    print(i,j)
        for row in rows:
            for j in range(n):
                matrix[row][j] = 0

        for col in cols:
            for i in range(m):
                matrix[i][col] = 0

                    
                   


        