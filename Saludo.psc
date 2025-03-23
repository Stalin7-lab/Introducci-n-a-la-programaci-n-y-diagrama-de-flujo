Algoritmo Saludo
	Definir nombre Como Caracter
	Definir opcion Como Caracter
	Repetir
		// Solicitar el nombre del usuario
		Escribir 'Por favor, ingrese su nombre:'
		Leer nombre
		// Validar que el usuario haya ingresado un nombre
		Mientras nombre='' Hacer
			Escribir 'Error: No puede dejar el nombre vacío. Intente de nuevo.'
			Escribir 'Por favor, ingrese su nombre:'
			Leer nombre
		FinMientras
		// Mostrar saludo personalizado
		Escribir '----------------------------------'
		Escribir '¡Hola, ',nombre,'! Bienvenido al sistema.'
		Escribir '----------------------------------'
		// Preguntar si desea ingresar otro nombre o salir
		Escribir '¿Desea ingresar otro nombre? (S/N)'
		Leer opcion
		opcion <- Mayusculas(opcion) // Convertir a mayúsculas para evitar errores
	Hasta Que opcion='N'
	Escribir 'Gracias por usar nuestro programa. ¡Hasta luego!'
FinAlgoritmo
