def function(n):
    return lambda a: a * n

mydoubler = function(2)
mytripler = function(3)

print(mydoubler(11))
print(mytripler(11))