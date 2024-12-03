import re


with open("day03/inputData.txt", "r", encoding="utf-8") as file:
    content = file.read().strip()

    ANSWER = 0
    matches =re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)",content)

    enabled = True

    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif match.startswith("mul") and enabled:
            # Extract numbers using a regular expression inside the loop
            numbers = re.findall(r"\d+", match)  # Extract all numbers from the 'mul(...)' string
            x, y = int(numbers[0]), int(numbers[1])
            ANSWER += x * y
#for line in content.split("\n"):

 #   matches = re.findall(pattern, line)

 #   total_sum = sum(int(x) * int(y) for x, y in matches)

#    ANSWER += total_sum
    #line = [int(x) for x in line.strip().split()]

print(ANSWER)
