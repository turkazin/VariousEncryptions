
p = int(input("p: "))
q = int(input("q: "))
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ 0123456789'
sozdikA_n = {alphabet[i]:i+1 for i in range(len(alphabet))}
sozdikN_a = {i+1:alphabet[i] for i in range(len(alphabet))}


n = p * q

fn = (p - 1) * (q - 1)



de = [(k * fn) + 1 for k in range(1,101)]
for i in range(len(de)):
    if i % (len(de)//20) == 0:
        print('\r')
    print(de[i], end=' ')

print()

half = {}
for i in de:
    factors = []
    for j in range(2, i//2):
        if (i % j == 0):
            factors.append(j)
    if len(factors) == 2:
        half[i] = factors

print()
counter = 0
for i in half:
    counter += 1
    if counter % 4 == 0:
        print('\r')
        counter = 0
    print(f"| {i:^2}: {half[i][0]:^3}, {half[i][1]:^3}\t ", end='')

print()

text = input("Текст енгізіңіз: ")



textNums = []
for i in range(len(text)):
    textNums.append(sozdikA_n[text.upper()[i]])
print(textNums)   



cipheredTexts = {}
for i in half:
    encryptedText = []
    for j in range(len(textNums)):
        var = (textNums[j]**half[i][0])%n
        encryptedText.append(var)
    cipheredTexts[i] = encryptedText
        
for i in cipheredTexts:
    print(f"(e = {half[i][0]}, d = {half[i][1]}), n = {n}: {cipheredTexts[i]}")




decipheredTexts = {}
for i in cipheredTexts:
    decryptedText = []
    for j in range(len(cipheredTexts[i])):
        decryptedText.append((cipheredTexts[i][j]**half[i][1])%n)
    
    decipheredTexts[i] = decryptedText


for i in decipheredTexts:
    print(f"(e = {half[i][0]}, d = {half[i][1]}), n = {n}: {decipheredTexts[i]}")



for i in decipheredTexts:
    textus = ''
    for j in range(len(decipheredTexts[i])):
        textus += sozdikN_a[decipheredTexts[i][j]]
        
    print(f"(e = {half[i][0]}, d = {half[i][1]}), n = {n}: {textus}")



print()
print("Белгісіз шифрды брутфорс арқылы шешу...")
print()
encryptedSeq = [322, 811, 573, 99, 1, 38]
print("Шифр: ",encryptedSeq)
print()
decryptedSeq = {}
for i in half:
    decrypt = []
    for j in range(len(encryptedSeq)):
        decrypt.append((encryptedSeq[j]**half[i][1])%n)
    decryptedSeq[i] = decrypt

for i in decryptedSeq:
    origText = ''
    try:
        for j in range(len(decryptedSeq[i])):
            origText += sozdikN_a[decryptedSeq[i][j]]
    except KeyError:
        pass
    finally:
        print(f"(e = {half[i][0]}, d = {half[i][1]}), n = {n}: {origText}")




