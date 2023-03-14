a = "Python 2023"
b = "Python 2023"
c = "Python 2023"

print(a == b)
print(b == c)

print(type(a), hex(id(a)))
print(type(b), hex(id(b)))
print(type(c), hex(id(c)))

print("---------------------------------------")

c = "Java 11"

print(a == b)
print(b == c)

print(type(a), hex(id(a)))
print(type(b), hex(id(b)))
print(type(c), hex(id(c)))


q1 = ["Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: ", "Oglądanie telewizji", "Czytanie książek", "słuchanie muzyki"]
q2 = ["W jakich okolicznościach czytasz książki najczęściej? ", "podczas podróży", "w czasie wolnym", "podczas pracy/nauki"]
q3 = ["Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? ", "chęć poszerzenia wiedzy", "czytanie to moje hobby", "czytanie mnie relaksuje"]
q4 = ["Po książki w jakiej formie sięgasz najczęściej?", "papierowej", "e-booki na komputerze", "e-booki na specjalnym czytniku"]
q5 = ["Ile książek czytasz średnio w ciągu roku? ", "0", "1-2", "3 lub więcej"]
q6 = ["Jak często czytasz książki", "codziennie", "raz w tygodniu", 'raz na miesiąc']
q7 = ["Po jakie gatunki książek sięgasz", "naukowe", "podróżnicze", "science fiction"]


print(q1[0])
print('1 ', q1[1])
print('2 ', q1[2])
print('3 ', q1[3])
q1a = int(input())

print(q2[0])
print('1 ', q2[1])
print('2 ', q2[2])
print('3 ', q2[3])
q2a = int(input())

print(q3[0])
print('1 ', q3[1])
print('2 ', q3[2])
print('3 ', q3[3])
q3a = int(input())

print(q4[0])
print('1 ', q4[1])
print('2 ', q4[2])
print('3 ', q4[3])
q4a = int(input())

print(q5[0])
print('1 ', q5[1])
print('2 ', q5[2])
print('3 ', q5[3])
q5a = int(input())

print(q6[0])
print('1 ', q6[1])
print('2 ', q6[2])
print('3 ', q6[3])
q6a = int(input())

print(q7[0])
print('1 ', q7[1])
print('2 ', q7[2])
print('3 ', q7[3])
q7a = int(input())

print("----------------------")

print(q1[0])
print(q1[q1a])
print("")

print(q2[0])
print(q2[q2a])
print("")

print(q3[0])
print(q3[q3a])
print("")

print(q4[0])
print(q4[q4a])
print("")

print(q5[0])
print(q5[q5a])
print("")

print(q6[0])
print(q6[q6a])
print("")

print(q7[0])
print(q7[q7a])
print("")

