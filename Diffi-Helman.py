
g = 5

Alp = 'ABCDE'

Secrets = {1:17, 2:19, 3:29, 4:31, 5:37}

primeNums = []
for i in range(3, 250):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
    if flag:
        primeNums.append(i)

possibleP = {}
for i in primeNums:
    p = 2 * i + 1
    if ((p-1) > g) and (((g**i)%p) != 1) and (p in primeNums):
        possibleP[i] = p
        
print("q\tp")
for i in possibleP:
    print(f"{i}\t{possibleP[i]}")

Opens = {}
for i in Secrets:
    Opens[i] = (g**Secrets[i])%possibleP[23]

for i in Opens:
    print(f"Y{Alp[i-1]}: {Opens[i]}")

Closeds = {}
for i in Secrets:
    d = {}
    for j in Opens:
        if i == j:
            continue
        d[f"Z({Alp[i-1]}{Alp[j-1]})"] = (Opens[j]**Secrets[i])%possibleP[23]
    Closeds[i] = d

    
for i in Closeds:
    print(f"{Alp[i-1]}: {Closeds[i]}")
        

