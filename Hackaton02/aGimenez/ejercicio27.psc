Proceso ejercicio27
	Definir numero1 Como Entero
	Definir numero2, suma Como Real
	numero1 = 0
	numero2 = 1
	suma = 0
	
	Mientras numero1 >= 0 Hacer
		Escribir "Ingresa cualquier numero positivo"
		Escribir "Finaliza con un numero Negativo"
		Leer numero1
		si numero1 >= 0 Entonces
			suma = suma + numero1
			numero2 = numero2 + 1
		FinSi
	FinMientras
	si numero2 > 0 Entonces
		Escribir "La media es: " suma/numero2
	FinSi
FinProceso
