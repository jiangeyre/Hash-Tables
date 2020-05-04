# Add up and print the sum of the all of the minimum elements of each inner array:

arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# The expected output is given by:

# 4 + -1 + 9 + -56 + 201 + 18 = 175

output = 0

for i in arr:
    
    output += min(i)
    
print(output)
