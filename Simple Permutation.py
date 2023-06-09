def write_table(text):
    factors = {}
    for i in range(2,len(text)//2):
        if len(text) % i == 0:
            if len(text)//i not in factors.keys() and abs(len(text)//i - i) < 5:
                factors[i] = len(text)//i
    return factors

text = input("Текст енгізіңіз: ")
print('\n'*2)

while not write_table(text):
    text += ' '

factors = write_table(text)

a = ()
for i in factors.keys():
    a += (i,factors[i])


print("-"*(a[1]*4+1))
for j in range(a[0]):

        print("|", end='')
        for k in range(a[1]):
            
            print(f"{text[a[1]*j+k]:^3}|", end='')


        print()
        print("-"*(a[1]*4+1))


d = ''
for j in range(a[1]):
        b = ''
        for k in range(a[0]): 
            b += text[j+k*a[1]]
        d += b 
print()
print('Шифрленген мәтін:', d)
