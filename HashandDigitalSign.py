alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
sozdikA_n = {alphabet[i]:i for i in range(len(alphabet))}

class Byte:
    def __init__(self, seq):
        if self.check_bit(seq):
            if len(seq) > 8:
                raise ValueError('Енгізілген мән 8 биттен жоғары!')
            elif len(seq) < 8:
                self.seq = '0'*(8 - len(seq)) + seq
            else:
                self.seq = seq

            
    @staticmethod
    def check_bit(seq):
        for i in seq:
            if i not in '01':
                raise ValueError("Енгізілген мән бит болып табылмайды!")
        return True

    def __iter__(self):
        return (i for i in self.seq)
    
    def __len__(self):
        return len(self.seq)

    def __getitem__(self, i):
        return self.seq[i]
    
    def __repr__(self):
        return f"{self.seq}"
    
    def __setitem__(self, key, value):
        pass
    
    def XOR(self, other):
        return Byte(''.join(['1' if other[i] != self.seq[i] else '0' for i in range(len((self.seq)))]))


def convert(value):
    if isinstance(value, int):
        bits = ''
        if value < 0:
            raise ValueError("Сан 0-ден үлкен болуы тиіс!")
        while True:
            l = value % 2
            if l == 1:
                bits += '1'
            else:
                bits += '0'
            value //= 2
            if value <= 0:
                break
        return Byte(bits[::-1])
                
    elif isinstance(value, Byte):
        num = 0
        for i in range(len(value)):
            num += int(value[i])*(2**(len(value)-1-i))
        return num
            
    else:
        raise TypeError("Белгісіз тип!")
        

p = int(input("p: "))
q = int(input("q: "))

text = input('Текст енгізіңіз: ').lower()

textConverted = [convert(sozdikA_n[i]) for i in text]

print()
for i in range(3):
    if i == 0:
        for i in range(len(text)):
            print("|", end='')
            print(f"{text[i].upper():^8}", end='|\t')
        print()
        continue
    if i == 1:
        for i in range(len(text)):
            print("|", end='')
            print(f"{sozdikA_n[text[i]]:^8}", end='|\t')
        print()
        continue
    if i == 2:
        for i in range(len(text)):
            print("|", end='')
            print(f"{textConverted[i]}", end='|\t')
        break
print()
fn = (p - 1) * (q - 1)

de = [(k * fn) + 1 for k in range(1,101)]


halfPrime = {}
for i in de:
    factors = []
    for j in range(2, i//2):
        if (i % j == 0) and j != p and j != q:
            factors.append(j)
    if len(factors) == 2:
        halfPrime[i] = factors


# print("Жартылай жай сандар және олардың бөлгіштері (e, d) : ")

# counter = 0
# for i in halfPrime:
#     counter += 1
#     if counter % 4 == 0:
#         print('\r')
#         counter = 0
#     print(f"{i}: {halfPrime[i][0]}, {halfPrime[i][1]}\t ", end='| ')


half = [[Byte('1111'+i[:len(i)//2]), Byte('1111'+i[len(i)//2:])] for i in textConverted]
Ms = [j for k in half for j in k]

print('\n Итерациялау кезеңі: ')

def iteration(M, n):
    Hs = Byte('0'*8)
    for i in range(len(text)*2):
        print(f"\n{i+1}-шы итерация: ")
        print(f"\t{M[i]}\n     (+)\n\t{Hs}\n\t{'-'*8}")
        mid = M[i].XOR(Hs)
        dec = convert(mid)
        print(f"\t{mid} = {dec}")
        san = (dec**2)%n
        Hs = convert(san)
        print(f"\t({dec}^2)mod({n}) = {san}\n\tH{i+1} = {Hs}")
        
  
    return convert(Hs)
        

ms = iteration(Ms, p*q)
print("\nХеш код m = ", ms)

d = int(input("d дешифрлаушы санды енгізіңіз: "))
print('d = ',d)
S = (ms**d)%(p*q)
print("ЭЦҚ S = ", S)


print("\n\nҚабылдаушы (M, S) жұбын алады және олардың айқындығын тексереді!\n\n")

e = int(input("е шифрлаушы санды енгізіңіз: "))
print('e = ',e)
mSht = (S**e)%(p*q)

print("m' = ", mSht)
if ms == mSht:
    print("m' = m")
    print("Қабылдаушы m' = m екеніне көз жеткізді, яғни (M, S) жұбының шындығы айқындалды!")