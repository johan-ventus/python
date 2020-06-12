from io import StringIO
import sys

def calculateSumAndDivisors(ordinal):
    triangle_numbers = []
    terms = []
    factor = 0

    def terms_output():
        return str((print(*terms, sep=',')))

    def printToFile():

        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result

        print(factor, end = ':')
        terms_output()

        sys.stdout = old_stdout
        result_string = result.getvalue()
        print(result_string)

        File_object = open("Divisors and sum of "+str(ordinal)+"th term.out", "w")
        File_object.write(result_string)

    for i in range(ordinal):
        triangle_numbers.append(i+1)
        factor = sum(triangle_numbers)

    for i in range(1, factor+1):
        if sum(triangle_numbers) % i == 0:
            terms.append(i)
    
    printToFile()
