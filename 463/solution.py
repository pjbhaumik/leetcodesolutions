class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid) #max number of rows
        cols = len(grid[0]) #max number of cols
        edges = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    edges += 4
                    below = i + 1
                    right = j + 1
                    if below < rows:
                        if grid[below][j] == 1:
                            edges -= 2
                    if right < cols:
                        if grid[i][right] == 1:
                            edges -= 2
        
        return edges  