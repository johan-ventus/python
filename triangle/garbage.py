ordinal = int(input('\nGimme the ordinal\n'))
triangle_numbers = []
terms = []

for i in range(ordinal):
    triangle_numbers.append(i+1)

#print(triangle_numbers)

factor = sum(triangle_numbers)
#print(factor)

for i in range(1, factor+1):
    if factor % i == 0:
        terms.append(i)

def function():
    return str((print(*terms, sep=',')))


#print(terms)
#print(factor)
#str((print(*terms, sep=',')))
#print(string)
#print("%s:%s" % (factor, print(*terms, sep=',')))




