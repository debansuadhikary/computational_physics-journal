# 1.Bubble Sort:
# Here we compare between the neighbouring numbers and shift the biggest among them towards a corner
L = [50,18,74,15,55,30,40,15,-2]

for i in range(len(L)): # for the number of passes
    for j in range(len(L) - i - 1): # compares the neighbours from the last
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]

L.reverse()
print("Bubble sort (descending):", L)

# 2.Insertion Sort:
# Here we arrange the numbers in an already arranged part of the list at the correct position.

M = [50,18,74,15,55,30,40,15,-2]

# first element is assumed sorted
for i in range(1, len(M)):
    key = M[i] # next element
    j = i-1
    while j >= 0 and M[j] > key:
        M[j+1] = M[j] # shifts larger elements right
        j -= 1
    M[j+1] = key

M.reverse()
print("Insertion sort (descending):", M)

