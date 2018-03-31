import random

def merge(A, B):
    final_sorted = [] #new list that will be sorted in the end
    length_A = len(A)
    length_B = len(B)
    i = 0
    j = 0
    while i < length_A and j < length_B: #do until we reach the end of either list A and B
        if A[i] <= B[j]: #if element B is less than element A
            final_sorted.append(A[i]) #then just add it to the final list
            i += 1 #to keep count where we are at in list A

        else: #otherwise, if A is greater than B
            global final_count
            final_count = final_count + (len(A) - i) # len(A) - i = how many reverse pairs at each iteration
            final_sorted.append(B[j])
            j += 1 #to keep count where we are at in list B

    if i == length_A: # No more elements to look at in A
        final_sorted.extend(B[j:]) #therefore, add elements in B to final_sorted since we already added A
    
    else: #if there are remaining elements in A
        final_sorted.extend(A[i:]) #then add them to the final list since we already added B
    return final_sorted 

def mergeSort(A):
    length = len(A)
    half_length = int(length/2)
    if length > 1:
        first_half = mergeSort(A[:half_length]) #keeps dividing the problem until one element remains
        second_half = mergeSort(A[half_length:]) #keeps dividing the other half of the problem until one element remains
        return merge(first_half,second_half) #recursively merge the individual elements
    else:
        return A

final_count = 0
random_list = []
i = 0
for i in range(100):
    random_list.append(random.randrange(0,250)) #genreate random numbers between 0 and 10,000
print(random_list)
mergeSort(random_list)
print("\n")
print("Reverse Pairs Count: ", final_count)