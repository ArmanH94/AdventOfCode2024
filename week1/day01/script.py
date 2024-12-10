from collections import Counter



with open("AoC_01/inputData.txt", "r", encoding="utf-8") as file:
    content = file.read().strip()

    left_table = []
    right_table = []
    for line in content.split("\n"):
        left, right = line.split( )
        left_table.append(int(left))
        right_table.append(int(right))
    

    left_table.sort()
    right_table.sort()

    answer = sum(abs(left - right) for left, right in zip(left_table, right_table))

    # right_table = Counter(right_table)
    # answer = 0

    # for lefty in left_table:
    #     answer += lefty * right_table[lefty]

print(answer)
