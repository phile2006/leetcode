class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        q = deque()
        q.append((0,0,1))
        if grid[0][0] ==1:
            return -1
        grid[0][0] = 1
        

        while q:
            r, c, d = q.popleft()
            if r == len(grid)-1 and c == len(grid[0])-1:
                return d
            else:
                for dr, dc in ((0,1), (1,1), (1,0),(0,-1),(-1,0),(-1,-1),(1,-1), (-1,1)):
                    row, col = r + dr, c + dc
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 1:
                        grid[row][col] = 1
                        q.append((row,col, d + 1)) 
        return -1