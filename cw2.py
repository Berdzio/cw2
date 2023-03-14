print("podaj pierwszą liczbe")
firstNumber = int(input())
print("podaj drugą liczbe")
secoundNumber = int(input())
print("podaj symbol działania")
whichSymbol = input()

if whichSymbol == '+':
    print(firstNumber + secoundNumber)
elif whichSymbol == '-':
    print(firstNumber - secoundNumber)
elif whichSymbol == '*':
    print(firstNumber * secoundNumber)
elif whichSymbol == '/':
    print(firstNumber / secoundNumber)
elif whichSymbol == '^':
    print(firstNumber ** secoundNumber)
elif whichSymbol == "%":
    print(firstNumber % secoundNumber)