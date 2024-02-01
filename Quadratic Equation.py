import math
def main():
    print("Welcome to the Quadratic Equation Calculator!")
    print()

    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    c = int(input('Enter the third number: '))

    D = (b ** 2) - (4 * a * c)

    if D >= 0:
        x1 = float((-b + math.sqrt(D)) / (2 * a))
        x2 = float((-b - math.sqrt(D)) / (2 * a))

        if x1.is_integer() and x2.is_integer():
            print(int(f"Fisrt root: {x1}"))
            print()
            print(int(f"Second root: {x2}"))


        else:
            print()
            print(f'Fisrt root: (-{b} + √{D}) / (2 * {a})')
            print(f'Second root: (-{b} - √{D}) / (2 * {a})')

    elif D <= 0:
        print()
        print('NO ROOOOOOTTTTSSSSS!!!!11!!!1!!1')

if __name__ == '__main__':
    main()