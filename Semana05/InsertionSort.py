vector = [1, 5, 2, 8, 7, 0, -1]

# This code is O(n²) because in the worst case we need to move for each element...
# ... in respective order: 
#  0, 1, 2,..., n-2, n-1
# Summing all costs we have:
# T(n) = 0 + 1 + 2 + ... + n-1
# What is the same as:
# T(n) = n(n-1)/2 

for i in range(0, len(vector)):
    actualIndex = i
    j = i-1
    while j >= 0 and vector[actualIndex] < vector[j]:
        temp = vector[actualIndex]
        vector[actualIndex] = vector[j]
        vector[j] = temp
        actualIndex = j
        j = j-1

print(vector)