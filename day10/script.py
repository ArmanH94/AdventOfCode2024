from collections import deque
answer = 0
grid = [[int(char) for char in line.strip()] for line in open("day10/inputData.txt")]
rows = len(grid)
cols = len(grid[0])

startPoints = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 0 ]

def findNines(grid, r, c):
    trails = 0
    myQueue = deque([(r,c)])
    seen = {(r,c):1}
    while len(myQueue) > 0:
        cr, cc = myQueue.popleft()
        if grid[cr][cc] == 9:
            trails += seen[(cr,cc)]
        for nr, nc in [(cr - 1,cc),(cr+1,cc),(cr,cc-1),(cr,cc+1)]: # Neighbours
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                continue
            if grid[nr][nc] != grid[cr][cc]+1:
                continue
            if (nr,nc) in seen:
                seen[(nr,nc)] += seen[(cr,cc)]
                continue
            seen[(nr,nc)] = seen[(cr,cc)]
            myQueue.append((nr,nc))
    return trails
    

print(sum(findNines(grid,r,c) for r,c in startPoints))