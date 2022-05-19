#Hacer un programa que permita saber si un año es bisiesto. 
#Para que un año sea bisiesto debe ser divisible por 4 y no debe
#ser divisible por 100, excepto que también sea divisible por 400.

print("como saber si un año es bisiesto")
print("---------------------------------")
print("Digite el año: ")
num=int(input())

if num%4==0 and num%100 != 0:
    print("El año es bisiesto")
elif num%4==0 and num%100 == 0 and num%400 == 0:
    print(" El Año es bisiesto")    
else:
    print("El Año no es bisiesto")