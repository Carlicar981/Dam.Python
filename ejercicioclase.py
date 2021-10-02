lista = list(range(1, 101))

print(lista)

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
         "Diciembre")


num = int(input("numero: "))

if (num > 0 and num <= len(meses)):
    print(meses[num - 1])
else:
    print("numero no valido")
