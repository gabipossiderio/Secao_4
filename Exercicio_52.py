print("BILHETE DE APOSTA")
apost1 = float(input("Valor investido pelo apostador 1:"))
apost2 = float(input("Valor investido pelo apostador 2:"))
apost3 = float(input("Valor investido pelo apostador 3:"))
odd = float(input("Agora, insira a odd utilizada:"))
print(f"Os apostadores receberão:\n"
      f"APOSTADOR 1:{apost1 * odd}\n"
      f"APOSTADOR 2: {apost2 * odd}\n"
      f"APOSTADOR 3: {apost3 * odd}")
