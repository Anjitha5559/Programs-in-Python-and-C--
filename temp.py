array_length = int(input("Plz enter the length of the array: "))
array = []
for i in range(array_length):
    element = int(input(f"Plz enter the element {i+1}: "))
    array.append(element)

def findMajorityCandidate(array):
    majority_element = 0
    count = 1  # Initialize count to 1
    for i in range(1, len(array)):  # Start from the second element
        if array[majority_element] == array[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            majority_element = i
            count = 1
    return array[majority_element]

def isMajority(array, candidate):
    count = 0
    for i in range(len(array)):
        if candidate == array[i]:
            count += 1
    if count > len(array) // 2:
        return True
    else:
        return False

def majorityElement(array, array_length):
    candidate = findMajorityCandidate(array)
    if isMajority(array, candidate):
        return candidate
    else:
        return -1

candidate = majorityElement(array, array_length)
if candidate != -1:
    print(f"The majority Element is {candidate}")
else:
    print("There is no majority element.")
