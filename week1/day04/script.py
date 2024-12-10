
import math
grid = open("day04/inputData.txt").read().splitlines()

answer = 0
#----------Part 1---------------:
# for r in range(len(grid)):
#     for c in range(len(grid[0])):
#         if grid[r][c] != "X":
#             continue
#         for dr in [-1, 0, 1]:
#             for dc in [-1, 0, 1]:
#                 if dr == dc == 0:
#                     continue
#                 if not (0 <= r + 3 * dr < len(grid) and 0 <= c + 3 * dc < len(grid[0])): continue
#                 if grid[r + dr][c + dc] == "M" and grid[r + 2 * dr][c + 2 * dc] == "A" and grid[r + 3 * dr][c + 3 * dc] == "S":
#                     answer += 1

#----------Part 2---------------:
for r in range(1, len(grid) - 1 ): # "A" cant be on the edge
    for c in range(1, len(grid[0]) - 1 ):
        if grid[r][c] != "A": continue
        corners = [grid[r-1][c-1], grid[r-1][c+1], grid[r+1][c+1], grid[r+1][c-1]]
        if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
            answer +=1

print(answer)
                