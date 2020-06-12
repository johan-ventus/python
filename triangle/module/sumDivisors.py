def calculateSumAndDivisors(ordinal):
    triangle_numbers = []
    terms = []
    factor = 0
    

    def terms_output():
        return str((print(*terms, sep=',')))


    for i in range(ordinal()):
        triangle_numbers.append(i+1)
        factor = sum(triangle_numbers)


    for i in range(1, factor+1):
        if sum(triangle_numbers) % i == 0:
            terms.append(i)

    print(factor, end = ':')
    terms_output()

def askOrdinal():
    return int(input('\nGimme the ordinal\n'))
