class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate(values: list):
            flag = 1
            for i in values:
                all_values = [j for j in i if j != "."]
                unique_values = set(all_values)
                if len(all_values) != len(unique_values):
                    return False
            return True
        
        rows = board
        columns = []
        cubes = []

        for i in range(9):
            columns.append(["."]*9)
            cubes.append([])

        for i in range(9):
            for j in range(9):
                columns[j][i] = board[i][j]
                cubes[(i//3)*3+(j//3)].append(board[i][j])

        return validate(rows) and validate(columns) and validate(cubes)
