# Demonstration of List and List Functions
numbers = [10, 20, 30, 40]

print("Original List:", numbers)

#max()
print("Maximum value",max(numbers))

#extend()
numbers.extend([50, 60, 70])

# append()
numbers.append(50)
print("After append:", numbers)

# insert()
numbers.insert(1, 15)
print("After insert:", numbers)

# remove()
numbers.remove(30)
print("After remove:", numbers)

# pop()
numbers.pop()
print("After pop:", numbers)

# sort()
numbers.sort()
print("After sort:", numbers)

# reverse()
numbers.reverse()
print("After reverse:", numbers)

# length
print("Length of list:", len(numbers))
