segundos = int(input("Informe quantos segundos deseja converter:"))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = (segundos % 3600) % 60
print(f'É equivalente a {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).')
