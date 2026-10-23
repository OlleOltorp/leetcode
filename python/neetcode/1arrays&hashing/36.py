# Time: O(1)
# Space: O(1)

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        squares = [set() for i in range(9)]
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == ",":
                    continue

                if val == ".":
                    continue

                squarenum = (row // 3) * 3 + (col // 3)

                if val in rows[row]:
                    return False

                if val in columns[col]:
                    return False

                if val in squares[squarenum]:
                    return False

                rows[row].add(val)
                columns[col].add(val)
                squares[squarenum].add(val)

        return True
