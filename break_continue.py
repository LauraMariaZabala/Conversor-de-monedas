#continue
def run():
    for contador in range(1000):
        if contador % 2 !=0: #si la division es diferente de cero entonces continua
            continue
        print(contador)

#break
    for i in range(10000):
        print(i)
        if i == 5678: #si i vale 5678 entonces break corta el ciclo
            break



        texto= input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o': #cuando el ciclo encuentre la letra o en el texto
            break        #corta el ciclo
        print(letra)

if __name__ == '__main__':
    run()

if __name__ == '__main__':
    run()

#el  ejemplo de arriba es como sacar los números pares (continue)