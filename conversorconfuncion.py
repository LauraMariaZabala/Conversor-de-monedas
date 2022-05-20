def conversor(tipoPesos, valorDolar):
    pesos = input("Cuantos pesos" + tipoPesos + "tienes?: ")
    pesos = float(pesos)
    dolar = pesos/ valorDolar
    dolar = round(dolar, 2)
    dolar =str(dolar)
    print("******************************")
    print("Tienes $ " + dolar + " dolarés")
    print("******************************")
    
menu = """
Bienvenido al conversor de monedas

Elige una opción.
***********************************
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos
***********************************
"""
opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 4048)
elif opcion ==2:
    conversor("Argentinos", 65)   
elif opcion ==3:
    conversor("Mexicanos", 24)   
else:
    print("Por favor seleccione una opción correcta")      
