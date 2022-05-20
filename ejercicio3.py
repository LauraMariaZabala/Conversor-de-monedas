print("Tributar impuesto")
print("*******************")
print("Digite su edad: ")
edad = int(input())
print("Digite su salario")
salario = int(input())

if edad >16 and salario >=5000000:
    print("Usted puede tributar")
else:
    print("Usted no puede tributar")