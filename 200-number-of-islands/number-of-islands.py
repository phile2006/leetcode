class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        queue = deque()
        marked = []
        count = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count +=1
                    visited.add((r,c))
                    queue.append((r,c))

                    while queue:
                        ro, co = queue.popleft()
                        for dr, dc in directions:
                            row , col = ro + dr, co + dc
                            if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == "1" and (row,col) not in visited:
                                visited.add((row,col))
                                queue.append((row,col))

        return count