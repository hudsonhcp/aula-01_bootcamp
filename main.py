#%%
print('Hello World!')

#%%
nome = input("Digite seu nome: ")
i = 0
for n in nome:
    if n == ' ':
        continue
    else:
        i += 1

print(f"Seu nome tem {i} letras.")
#%%
nome = input("Digite seu nome: ")

nome_lista = nome.split(' ')
i = 0
for n in nome_lista:
    i += len(n)

print(f"Seu nome tem {i} letras.")

#%%
print(sum([float(input('Digite um número: ')),float(input('Digite outro número: '))]))
#%%
numero_1 = float(input('Digite um número: '))
numero_2 = float(input('Digite outro número: '))

soma = numero_1 + numero_2

print(f"A soma dos números é: {soma}")

#%%

CONSTANTE = 1000

nome = input('Digite seu nome: ')

salario = float(input('Digite seu salário: '))

bonus = float(input('Digite o bônus(%): '))/100

kpi_bonus = CONSTANTE + salario * bonus

print(f"{nome}, seu KPI Bônus é de R$ {kpi_bonus:.2f}")