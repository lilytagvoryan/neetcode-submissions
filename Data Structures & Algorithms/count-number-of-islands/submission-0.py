class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # No islands if grid is empty
        if not grid:
            return 0

        # Get dims of grid, cells visited, island counts
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        # Run bfs on land cell; mark visited and add to queue
        def bfs(r, c):
            queue = collections.deque()
            visit.add((r, c))
            queue.append((r, c))
            # While queue not empty, check cells in all directions
            while queue:
                row, col = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc                
                    # Check if cell is in-bound, land, unvisited;
                    # then add to queue and mark visited
                    if (r in range(rows) and c in range(cols) and
                        grid[r][c] == "1" and (r, c) not in visit):
                        queue.append((r, c))
                        visit.add((r, c))

        # Visit every position in grid then run bfs and add islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands  

