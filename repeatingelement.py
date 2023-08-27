array_length = int(input("Plz enter the length of the array :"))
array = []
for i in range(array_length):
    element = int(input(f"Plz enter the variable {i+1} :"))
    array.append(element)
    
def findMajorityCandidate(array):
    majority_element = 0
    count = 1   
    for i in range (1,len(array)):
        if(array[majority_element]==array[i]):
            count += 1
        else:
            count -=1
        if(count==0):
            majority_element = i
            count = 1
    return array[majority_element]
    
    
def isMajority(array,candidate):
    count = 0
    for i in range(len(array)):
        if(candidate==array[i]):
            count += 1
    if(count>array_length//2):
        return True
    else:
        return False
    
    
def majorityElement(array,array_length):
    candidate = findMajorityCandidate(array)
    if(isMajority(array,candidate)==True):
        return candidate
    else:
        return -1
candidate = majorityElement(array,array_length)
print(f"The majority Element is {candidate}")
#This Algorithm is called Moore's Voting algorithm
#Eventhough it can be done through brite force, this is the most efficient method
# Steps to implement the algorithm :
# Step 1 – Find a candidate with the majority –

# Initialize a variable say i ,votes = 0, candidate =-1 
# Traverse through the array using for loop
# If votes = 0, choose the candidate = arr[i] , make votes=1.
# else if the current element is the same as the candidate increment votes
# else decrement votes.
# Step 2 – Check if the candidate has more than N/2 votes –

# Initialize a variable count =0 and increment count if it is the same as the candidate.
# If the count is >N/2, return the candidate.
# else return -1.      
    