with open("day02/inputData.txt", "r", encoding="utf-8") as file:
    content = file.read().strip()
    answer = 0

def check(line):
    g = all(a > b for a,b in zip(line, line[1:])) or all(a < b for a,b in zip(line, line[1:]))
    if g:
        line.sort()
        for a,b in zip(line, line[1:]):
            if b - a > 3 or b - a < 1:
                g = False
                break
    return g

for line in content.split("\n"):
    line = [int(x) for x in line.strip().split()]
    if check(line) or any(check(line[:i] + line[i+1:]) for i in range(len(line))):
        answer += 1
print(answer)
