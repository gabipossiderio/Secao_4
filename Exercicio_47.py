num = int(input("Informe um número inteiro de quatro dígitos:"))

if 1000 <= num <= 9999:
    t = str(num)
    print(f" {t[0]}\n {t[1]}\n {t[2]}\n {t[3]}\n")
else:
    print(f"O número informado não possui quatro dígitos,"
          f"tente novamente inserindo um número de três dígitos.")
