answer = 0


def get_pairings(keyPairings):
    pairings = {}
    for line in keyPairings.strip().split("\n"):
        key, value = map(int, line.split("|"))  # Split each line and convert to int
        if key in pairings:
            pairings[key].append(value)  # Add to the existing list if key exists
        else:
            pairings[key] = [value]  
    return pairings

#----------Part 1---------------:
# for sequence in sequences.strip().split("\n"):
#     sequence = ([int(x) for x in sequence.split(',')])
#     correctOrder = True
#     for current in range(len(sequence)):
#         CurrentValue = sequence[current]
#         if CurrentValue not in pairings and current != len(sequence)-1:
#             correctOrder = False
        
#         if correctOrder:
#             mylist = pairings.get(sequence[current])

#             for successor in range(current+1, len(sequence)): # Successors, right of current
#                 SuccessorValue = sequence[successor]
#                 if SuccessorValue not in mylist:
#                     correctOrder = False

#     if correctOrder:
#         answer += sequence[len(sequence)//2]

#----------Part 2---------------:   
def find_unsorted(sequences, pairings):
    unsorted_sequences = []     
    for sequence in sequences.strip().split("\n"):
        sequence = ([int(x) for x in sequence.split(',')])
        correctOrder = True
        for current in range(len(sequence)):
            CurrentValue = sequence[current]
            if CurrentValue not in pairings and current != len(sequence)-1:
                correctOrder = False
            
            if correctOrder:
                mylist = pairings.get(sequence[current])

                for successor in range(current+1, len(sequence)): # Successors, right of current
                    SuccessorValue = sequence[successor]
                    if SuccessorValue not in mylist:
                        correctOrder = False

        if not correctOrder:
            unsorted_sequences.append(sequence)

    return unsorted_sequences



def sort_sequences(unsorted_sequences, pairings):
    answer = 0
    for unsorted_sequence in unsorted_sequences:
        reordered_sequence = []
        remaining = set(unsorted_sequence)

        while remaining:
            for value in remaining:
                # Check if the current value has all remaining values (minus itself) in its pairing list
                if all(other in pairings.get(value, []) for other in remaining if other != value):
                    reordered_sequence.append(value)
                    remaining.remove(value)
                    break  # Move to the next round

        #sorted_sequences.append(reordered_sequence)
        answer += reordered_sequence[len(reordered_sequence)//2]
    return answer

if __name__ == "__main__":
    content = open("day05/inputData.txt").read().splitlines()
    keyPairings, sequences = open("day05/inputData.txt").read().split("\n\n")
    pairings = get_pairings(keyPairings)
    unsorted = find_unsorted(sequences,pairings)
    answer = sort_sequences(unsorted,pairings)

    print(answer) 


                