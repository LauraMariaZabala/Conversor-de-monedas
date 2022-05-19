def prueba(mensaje):
    print("Hola!!!")
    print("Como estas?")
    print(mensaje)
    print("Adios")


opcion= int(input("Elige una opción {1,2,3}; "))

if opcion == 1:
    prueba("Elegiste la opción 1")
elif opcion == 2:
    prueba("Elegiste la opción 2")
elif opcion == 3: 
    prueba("Elegiste la opcion 3")
else:
    print("Por favor elige una opción correcta")            