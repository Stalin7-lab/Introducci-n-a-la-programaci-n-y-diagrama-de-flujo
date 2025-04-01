#comprueba si un caracter ingresado es una vocal(a,e,i,o,u)

caracter = input("Ingresa un solo carácter: ").strip().lower()
if len(caracter) == 1 and caracter in "aeiou":
    print("El carácter ingresado es una vocal.")
else:
    print("El carácter ingresado no es una vocal o no es válido.")