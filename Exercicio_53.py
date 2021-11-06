comp = int(input("Insira o comprimento do terreno:"))
larg = int(input("Insira a largura do terreno:"))
tela = int(input("Agora, complete com o valor do metro da tela:"))
per = comp*2 + larg*2
print(f"Você gastará {per * tela} reais para cercar este terreno.")
