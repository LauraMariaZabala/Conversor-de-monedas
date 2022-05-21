print("Bienvenido/a ")
print("Digite la presion sistolica: ")
sistolica = int(input())
print("Digite la presion diastolica: ")
diastolica = int(input())

if (sistolica <72 and diastolica <65):
    print("Alerta amarilla: hipotension ")
elif (sistolica >=72 and sistolica <107) and (diastolica >=65 and diastolica <73):
    print("Alerta verde: presion arterial optima")      
elif (sistolica >=107 and sistolica <124) and (diastolica >=73 and diastolica <81):
    print("Alerta verde: presion arterial normal")    
elif(sistolica >=124 and sistolica <138) and (diastolica >=81 and diastolica <93):   
    print("Alerta amarilla: prehipertension")
elif(sistolica >= 138 and sistolica <156) and(diastolica >= 93 and diastolica <102):
    print("Alerta naranja: HTA grado 1")
elif(sistolica >= 156 and sistolica <175) and (diastolica >= 102 and diastolica <114):
    print("Alerta roja: HTA grado 2")
elif(sistolica >= 175 and diastolica >=114):
    print("Alerta roja: HTA grado 3")
elif(sistolica >=140 and diastolica <90):
    print("Alerta naranja: hipertension sistolica aislada") 
else:
    print("Alerta gris: no se puede mostrar la categoria.")        


