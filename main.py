# Задача:
# Даны две строки. Эти строки между собой отличаются только одним символом.
# Вторая строка получена путём добавления случайного символа в случайную позицию в первой строке.
# Вывести данный символ и его индекс.


someString = 'kufar'
someString2 = 'kufayr'

lenString2 = len(someString2)

index = 0
indexSymbol = 0

while index < lenString2:
    if someString2[index] not in someString:
        indexSymbol = someString2.index(someString2[index])

    index += 1

print(someString2[indexSymbol])
print(indexSymbol)
