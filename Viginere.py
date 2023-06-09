alphabet = "АӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШЩЪЫІЬЭЮЯ"
sozdikA_n = {alphabet[i]:i for i in range(len(alphabet))}
sozdikN_a = {i:alphabet[i] for i in range(len(alphabet))}


def getMass(text):
    return [i.upper() for i in text.replace(',', '').\
                 replace('.', '').replace('- ', '').split(' ')]

def genKeys(key, text):
    keys = []
    for i in text:
        if len(key) > len(i):
            keys.append(key[:len(i)])
        elif len(key) < len(i):
            keys.append(key + key[:len(i)-len(key)])
        else:
            keys.append(key)
    return keys

def numberize(array):
    flag = False
    for i in array:
        if isinstance(i, str):
            flag = True
            break
    
    if flag:
        return [[sozdikA_n[j] for j in i] for i in array]
    
    return ' '.join([''.join([sozdikN_a[j] for j in i]) for i in array])

def cipher(text, keys):
    a = []
    if flag == 'cip':
        for i in range(len(text)):
            c = []
            for j in range(len(text[i])):
                c.append((text[i][j]+keys[i][j])%len(alphabet))
            a.append(c)
    else:
        for i in range(len(text)):
            c = []
            for j in range(len(text[i])):
                c.append((text[i][j]-keys[i][j])%len(alphabet))
            a.append(c)
    return a



flag = ''
while True:
    flag = input("Шифрлау үшін (cip), ал дешифрлау үшін (decip) енгізіңіз, ал шығу үшін (exit): ").replace(' ', '')
    if flag == 'cip' or flag == 'decip':
        break
    elif flag == 'exit':
        exit()
    print("Енгізілген мән қате! Қайталаңыз!")


Text = getMass(input("Текст енгізіңіз: ").upper())
Keys = genKeys(input('Кілт енгізіңіз: ').upper(), Text)
numsText = numberize(Text)
numsKeys = numberize(Keys)


cipherText = numberize(cipher(numsText, numsKeys))
if flag == 'cip': 
    print(f"Шифрленген текст: {cipherText}"); 
else: 
    print(f"Дешифрленген текст: {cipherText}")