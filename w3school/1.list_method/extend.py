fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)

print(fruits)


'''
extend vs append

append output:   ['apple', 'banana', 'cherry', (1, 4, 5, 9)]
extend output:   ['apple', 'banana', 'cherry', 1, 4, 5, 9]
'''