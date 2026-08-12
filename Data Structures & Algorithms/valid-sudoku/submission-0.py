class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(9):
            row = []
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                if value in row:
                    return False
                row.append(value)

        #columns
        for i in range(9):
            col = []
            for j in range(9):
                value = board[j][i]
                if value == ".":
                    continue
                if value in col:
                    return False
                col.append(value)

        #grid
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                grid = set()
                for i in range(3):
                    for j in range(3):
                        value = board[r + i][j + c]
                        if value == ".":
                            continue
                        if value in grid:
                            return False
                        grid.add(value)
            
        return True