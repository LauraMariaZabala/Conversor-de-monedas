def palindromo(palabra):
    palabra = palabra.replace(' ','') #remplaza  o elimina los espacios
    palabra = palabra.lower() #pone todas las palabras en minusculas
    palabra_invertida = palabra[::-1] # se genera la palabra invertida

    if palabra == palabra_invertida: #si la palabra se lee al derecho y al reves
        return True                  #devuelve true
    else:
        return False                 #si no devuelve false


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
       print('No es palindromo')


if __name__ == '__main__':
    run()