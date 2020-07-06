class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Go from end points starting with the 'O's and do bfs
        # until you reach all of the 'O's
        if len(board) < 1 or len(board[0]) < 1:
            return
        posMoves = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        for row in range(len(board)):
            if board[row][0] == 'O':
                visited.add((row,0))
            if board[row][-1] == 'O':
                visited.add((row,len(board[0])-1))
        for col in range(len(board[0])):
            if board[0][col] == 'O':
                visited.add((0,col))
            if board[-1][col] == 'O':
                visited.add((len(board)-1,col))
        queue = list(visited)
        while queue:
            newQueue = []
            for row, col in queue:
                for x, y in posMoves:
                    newRow = row + x
                    newCol = col + y
                    if 0 <= newRow < len(board) and 0 <= newCol < len(board[0]) and (newRow, newCol) not in visited and board[newRow][newCol] == 'O':
                        newQueue.append((newRow, newCol))
                        visited.add((newRow, newCol))
            queue = newQueue
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in visited:
                    board[row][col] = 'X'