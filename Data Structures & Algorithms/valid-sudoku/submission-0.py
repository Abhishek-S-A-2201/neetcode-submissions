class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(nums):
            chars = set()
            for i in nums:
                if i == '.':
                    continue
                if i in chars:
                    return False
                chars.add(i)
            return True
        
        rows = board[::]
        cols = [[] for i in range(9)]
        blocks = [[] for i in range(9)]

        for row in range(9):
            for col in range(9):
                cols[col].append(board[row][col])
                blocks[3*(col//3)+row//3].append(board[row][col])
        
        for i in [rows, cols, blocks]:
            for j in i:
                if valid(j):
                    continue
                else:
                    return False
        
        return True

            
