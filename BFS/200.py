class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        posMoves = [(1,0), (0,1), (-1,0), (0,-1)]
        numIsland = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row,col) not in visited:
                    queue = [(row,col)]
                    visited.add((row,col))
                    numIsland += 1
                    while queue:
                        x0, y0 = queue.pop()
                        for x1, y1 in posMoves:
                            newX = x0 + x1
                            newY = y0 + y1
                            if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] == '1' and (newX, newY) not in visited:
                                visited.add((newX, newY))
                                queue.append((newX, newY))
        return numIsland