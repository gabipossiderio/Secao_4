print("FOLHA DE PAGAMENTO")
print("Funcionário: José da Silva")
sal = float(input("Informe seu salário base em R$:"))
print(f"Receberá R$ {sal + (sal * 0.05) - (sal * 0.07)} considerando o desconto de 7% do IR e sua gratificação de 5%.")
