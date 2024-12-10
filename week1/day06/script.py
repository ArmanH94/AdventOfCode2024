grid = list(map(list,open("day06/inputData.txt").read().splitlines()))
rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            break
    else:
        continue
    break

def loops(grid, r, c):
    dr = -1
    dc = 0

    seen = set()
    while True: #Two exit conditions: going of the grid, OR finding ourselves in a loops
        seen.add((r, c, dr, dc))

        if r+dr < 0 or r+dr >= rows or c+dc < 0 or c+dc >= cols:
            return False #Exits the while-loop if we go outside the grid

        #Either change dir OR move 1 tile
        if grid[r+dr][c+dc] == '#':
            dc, dr = -dr, dc #change directions
        else: #move 1 tile
            r +=dr
            c += dc
        # If we find ourselfs in a position with the same direction as we've been been before
        # we are in a loop, and can exit. 
        if (r,c,dr,dc) in seen:
            return True

count = 0

for cr in range(rows):
    for cc in range(cols):
        if grid[cr][cc] != ".":
            continue
        grid[cr][cc] = "#" # WE set it to an obstacle
        if loops(grid, r, c):
            count +=1
        grid[cr][cc] = "."
    
print(count)


