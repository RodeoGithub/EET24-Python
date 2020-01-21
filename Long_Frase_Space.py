def e1():
	frase=str(input("Ingrese una frase: "))
	print("La longitud de la frase es: ", len(frase))
	e=0
	for i in range (0, len(frase)):
		if(frase[i]==' '):
			e=e+1
	print("La cantidad de espacios es: ", e)
