print("HORÁRIO DA EXPERIÊNCIA")
hor = int(input("hora(s):"))
minu = int(input("minuto(s):"))
seg = int(input("segundo(s):"))
duracao = int(input("Qual é a duração da experiência em segundos?"))

hora1 = hor * 3600
minuto2 = minu * 600
tempo1 = hora1 + minuto2 + seg + duracao

horas = tempo1 // 3600
minutos = (tempo1 % 3600) // 60
segundos = (tempo1 % 3600) % 60

if horas > 24:
    print(f"A experiência terminará às {horas - 24} hora(s), {minutos} minuto(s) e {segundos} segundo(s).")

else:
    print(f"A experiência terminará às {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).")
