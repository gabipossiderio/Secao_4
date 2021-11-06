num = (input("Digite um número inteiro positivo de três digitos:"))
if 100 <= int(num) <= 999:
    print(f"Esse número em sua versão invertida é {(num[::-1])}")
else:
    print("Insira um número de três digitos, por favor!")
