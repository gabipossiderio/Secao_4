valor = float(input("Digite o valor a ser pago:"))
desconto = valor * 0.10
valor_desconto = valor - desconto
print(f"Total com desconto de 10%:{valor - desconto}.")
print(f"Valor de cada parcela em 3x sem juros: {valor / 3 }.")
print(f"Comissão do vendedor em caso de venda à vista: {valor_desconto * 0.05}.")
print(f"Comissão do vendedor em caso de venda parcelada: {valor * 0.05}.")
