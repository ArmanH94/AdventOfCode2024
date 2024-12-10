#---------Part 1--------
# total = 0

# def can_obtain(target, array):
#     if len(array) == 1: #The last remaining number equals the remaining target 81|81
#         return target == array[0]
#     if target % array[-1] == 0 and can_obtain(target // array[-1], array[:-1]):
#         return True
#     if target > array[-1] and can_obtain(target - array[-1], array[:-1]):
#         return True

# for line in open("day07/inputData.txt"):
#     left, right = line.split(": ")
#     target = int(left)
#     array = [int(x) for x in right.split()]
#     if can_obtain(target, array):
#         total += target
# print(total)


#---------Part 2--------
total = 0

def can_obtain(target, array):
    if len(array) == 1: #The last remaining number equals the remaining target 81|81
        return target == array[0]
    if target % array[-1] == 0 and can_obtain(target // array[-1], array[:-1]):
        return True
    if target > array[-1] and can_obtain(target - array[-1], array[:-1]):
        return True
    
    s_target = str(target) #string of target
    s_last = str(array[-1]) # string of last value in array

    if len(s_target) > len(s_last) \
    and s_target.endswith(s_last) \
    and can_obtain(int(s_target[:-len(s_last)]),array[:-1]):
        return True

for line in open("day07/inputData.txt"):
    left, right = line.split(": ")
    target = int(left)
    array = [int(x) for x in right.split()]
    if can_obtain(target, array):
        total += target

print(total)