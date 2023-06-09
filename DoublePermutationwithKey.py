import random as r

def write_table(text):
    factors = {}
    for i in range(2,len(text)//2):
        if len(text) % i == 0:
            if len(text)//i not in factors.keys() and abs(len(text)//i - i) < 5:
                factors[i] = len(text)//i
    return factors

def randomrange(n):
    mass = [i for i in range(1,n+1)]
    r.shuffle(mass)
    return mass

text = input("Текст енгізіңіз: ")
print('\n'*2)

while not write_table(text):
    text += ' '

factors = write_table(text)

a = ()
for i in factors.keys():
    a += (i,factors[i])


randRows = randomrange(a[0])
randColumns = randomrange(a[1])

print("Баған: ", randColumns)
print("Қатар: ", randRows)
print()

textMass = {randRows[j]:{randColumns[i]:text[a[1]*j+i] for i in range(a[1])} for j in range(a[0])}



def showCol():
    print(' '*3, end='')
    for i in randColumns:
        print(f"{i:^3}", end=' ')
    print()
    print("-"*(a[1]*4+3))
    for i in randRows:
        print(f"{i} |", end='')
        for j in randColumns:
            print(f"{textMass[i][j]:^3}|", end='')
        print()
        print("-"*(a[1]*4+3))
    print()

showCol()
randColumns.sort()
showCol()
randRows.sort()
showCol()

b = ''
for i in randColumns:
    for j in randRows:
        b += textMass[j][i]
print(f"Шифртекст: '{b}'")