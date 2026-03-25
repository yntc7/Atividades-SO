num = float(input("Digite o primeiro número: "))
while num < 0:
    num = float(input("Número inválido! Digite novamente: "))

maior = num
menor = num

for i in range(2, 101):
    num = float(input(f"Digite o próximo número: "))
    
    while num < 0:
        num = float(input("Valor inválido! Digite novamente: "))
    
    if num > maior:
        maior = num
    
    if num < menor:
        menor = num

print("Maior valor: ", maior)
print("Menor valor: ", menor)