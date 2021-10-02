import math
def media(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)

def desviacion_std(lista):
    prom = media(lista)
    n = len(lista)
    suma = 0
    for i in lista:
        suma += (i - prom)**2
    return math.sqrt(suma / (n-1))

def main():
    num_elem = int(input())
    lista = []
    if num_elem > 0:
        for i in range(num_elem):
            lista.append(int(input()))
        print(f"Media: {media(lista)}")
        print(f"Desviacion Estándar: {desviacion_std(lista):.2f}")
    else:
        print('Error')

if __name__=='__main__':
    main()
