n, k = input().split(" ")
L = [int(x) for x in input().split()]
L_modulo, result = [] ,[]

for i in range(len(L)):
    L_modulo.append(L[i] % 87)
for i in range(len(L)):
    j = L_modulo.index(max(L_modulo))
    result.append(L[j])
    L_modulo[j] = 0

print(result)
