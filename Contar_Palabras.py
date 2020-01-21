def e1():
	frase=str(input("Ingrese una frase: "))
	if(len(frase)!=0):
                count=1
                for i in range (0,len(frase)):
                        if(frase[i]==" "):
                                count=count+1
                print("Hay ", count, " palabras")
        else:
                print("No hay palabras")
