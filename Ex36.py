num = int(input("Digite um número: "))
soma = 1
fat = 1

for i in range(1, num + 1):
    fat = fat * i
    soma += 1 / fat

print(f"Resultado da série: {soma:.2f}")    
