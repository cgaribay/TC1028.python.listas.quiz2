![Tec de Monterrey](../../images/logotecmty.png)
# Media y desviación estándar
### Tema Listas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Escribe un programa que primero lea la cantidad de elementos que vas a ingresar en la lista y después acepte cada uno de los elementos. Todos los datos que se ingresan deben ser números enteros. Si el usuario pone un número menor a uno se imprimirá un mensaje de error.

Posteriormente, el programa debe calcular la media (promedio) y la desviación estándar y desplegarlos en la terminal.

**Importante:** Utiliza dos funciones, una llamada media y otra llamada desviacion_std, que reciben como parámetro de entrada una lista y regresan como resultado la media y la desviación estándar respectivamente.

**Cómo se calcula la desviación estándar:** Para una lista de 6 elementos y donde la media (promedio) de esos elementos es 6.33 la desviación estándar se calcula así: 

![Desviación Estándar](../../images/desviacion_std.PNG)

## Entrada
Un número entero que representa la cantidad de valores que tiene la lista, asi como cada uno de los valores de la lista.

## Salida
Un mensaje que muestre la media y la desviación estándar. Observa que tanto la media como la desviación estándar son valores **flotantes**.
 
## Ejemplo de ejecución del programa:
### Entrada
```
>>>0
```
### Salida
```
Error
```
### Entrada
```
>>>5
>>>1
>>>4
>>>7
>>>2
>>>3
```
### Salida
```
Media: 3.4
Desviación Estándar: 2.30
```

### Entrada
```
>>>4
>>>3
>>>8
>>>5
>>>2
```
### Salida
```
Media: 4.5
Desviación Estándar: 2.65
```
No uses letreros para pedir los datos y diseña los letreros de salida iguales a los del ejemplo.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
