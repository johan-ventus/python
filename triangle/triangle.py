def main():
    ordinal = int(input('\nGimme the ordinal\n'))
    triangle_numbers = []
    terms = []

    for i in range(ordinal):
        triangle_numbers.append(i+1)

    print(triangle_numbers)

    factor = sum(triangle_numbers)

    for i in range(1, factor+1):
        if factor % i == 0:
            terms.append(i)

    def function():
        return str((print(*terms, sep=',')))

    print(factor, end = ':')
    function()

if __name__ == "__main__":
    main()
