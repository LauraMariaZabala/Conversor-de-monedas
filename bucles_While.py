def run():
    LIMITE = 1000000 #constante con el valor de 1000
    contador = 0 #contador que inicia en cero

    potencia_2 = 2**contador #esta variable tiene el 2 elevado a cero   
                            #que es como inicia el contador (0)

    while potencia_2 < LIMITE: #si la potencia es menor a 1000 entonces
        print('2 elevado a ' + str(contador) + ' es igual a ' + str(potencia_2)) #se repite este print
        contador=contador + 1 #si potencia vale mas de 1000 se rompe
        potencia_2 = 2**contador


if __name__ == '__main__':
    run()
