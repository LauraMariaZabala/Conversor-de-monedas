print("Definir si la letra ingresada es vocal")
print("Digite un letra :")

letra = input()

if letra == "a" or letra == "A" and letra == "e" or letra == "E" and letra == "i" or letra == "I" and letra == "o" or letra == "O" and letra == "u" or letra == "U" :
    print("La letra es vocal ")
elif len(letra) !=1:
    print("No se puede procesar el dato")
else:
    print("La letra no es vocal") 

