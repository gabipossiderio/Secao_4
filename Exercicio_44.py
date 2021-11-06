d = float(input("Insira a altura do degrau da escada:"))
a = float(input("Agora, insira a altura que deseja alcançar subindo a escada:"))
distancia = int(a/d)
if a % d > 0:
    print(f"Você precisará subir {distancia + 1} degraus para alcançar a altura desejada.")
else:
    print(f"Você precisará subir {distancia} degraus para alcançar a altura desejada.")
