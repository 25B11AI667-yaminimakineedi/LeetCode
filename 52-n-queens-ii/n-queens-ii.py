class Solution:
    def totalNQueens(self, n: int) -> int:
        count=0
        board=[["."]*n for _ in range(n)]
        def issafe(row,col):
            for j in range(col):
                if board[row][j]=="Q":
                    return False
            i,j=row-1,col-1
            while i>=0 and j>=0:
                if board[i][j]=="Q":
                    return False
                i-=1
                j-=1
            i,j=row+1,col-1
            while i<n and j>=0:
                if board[i][j]=="Q":
                    return False
                i+=1
                j-=1
            return True
        def sol_queens(col):
            nonlocal count
            if col>=n:
                count+=1
                return
            for row in range(n):
                if(issafe(row,col)):
                    board[row][col]="Q"
                    sol_queens(col+1)
                    board[row][col]="."
        sol_queens(0)
        return count       