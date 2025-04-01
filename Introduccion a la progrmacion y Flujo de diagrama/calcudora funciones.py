#crear una calculadora usando funciones

def suma(a,b):
    return a + b

def resta(a,b):
    return a * b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b !=0:
        return a / b
    else:
        return "error: no se puede dividir por cero."
    
print("seleccione una operacion:")
print("1.sumar")
print("2.restar")
print("3.multiplicar")
print("4.dividir")

operacion= input("ingrese el numero de la operacion (1/2/3/4):")

num1= float(input("ingrese el primer numero:"))
num2= float(input("ingrese el segundo numero:"))

if operacion =="1":
    print("resultado: {suma(num1, num2)}")

elif operacion == "2":
    print("resultado: {resta(num1, num2)}")

elif operacion == "3":
    print("resultado: {multiplicacion(nume1,num2)}")

elif operacion == "4":
    print("resultado: {division(num1, numer2)}")

else:
    print("operacion no valida")