"""
This program can sum, subtract, multiply, divide, show major and minor, show even and odd,
show average and show how many vowels appear in a sentence.
"""

def ej():
	op=int(input("Elija una opción entre 1 y 9: "))
	op1="OPCIÓN 1: Sumar 2 numeros"
	op2="OPCIÓN 2: Restar 2 numeros"
	op3="OPCIÓN 3: Multiplicar 2 numeros"
	op4="OPCIÓN 4: Dividir 2 numeros"
	op5="OPCIÓN 5: Informar cual es mayor y cual menor entre 2 numeros"
	op6="OPCIÓN 6: informar cual es par y cual impar entre 2 numeros"
	op7="OPCIÓN 7: Informar el promedio de 3 numeros"
	op8="OPCIÓN 8: Informar la cantidad de cada vocal en una frase"
	op9="OPCIÓN 9: Cerrar programa"
	print(op1)
	print(op2)
	print(op3)
	print(op4)
	print(op5)
	print(op6)
	print(op7)
	print(op8)
	print(op9)
	while(op!=9):
		if (op==1):
			a=int(input("ingrese el primer numero: "))
			b=int(input("ingrese el segundo numero: "))
			print("El resultado de la suma es: ",a+b)
			print(op1)
			print(op2)
			print(op3)
			print(op4)
			print(op5)
			print(op6)
			print(op7)
			print(op8)
			print(op9)
			op=int(input("Elija una opción entre 1 y 9: "))
		if (op==2):
			a=int(input("ingrese el primer numero: "))
			b=int(input("ingrese el segundo numero: "))
			print("El resultado de la resta es: ",a-b)
			print(op1)
			print(op2)
			print(op3)
			print(op4)
			print(op5)
			print(op6)
			print(op7)
			print(op8)
			print(op9)
			op=int(input("Elija una opción entre 1 y 9: "))
		if (op==3):
			a=int(input("ingrese el primer numero: "))
			b=int(input("ingrese el segundo numero: "))
			print("El resultado de la multiplicacion es: ",a*b)
			print(op1)
			print(op2)
			print(op3)
			print(op4)
			print(op5)
			print(op6)
			print(op7)
			print(op8)
			print(op9)
			op=int(input("Elija una opción entre 1 y 9: "))
		if (op==4):
			a=int(input("ingrese el primer numero: "))
			b=int(input("ingrese el segundo numero: "))
			print("El resultado de la division es: ",a/b)
			print(op1)
			print(op2)
			print(op3)
			print(op4)
			print(op5)
			print(op6)
			print(op7)
			print(op8)
			print(op9)
			op=int(input("Elija una opción entre 1 y 9: "))
		if (op==5):
			a=int(input("ingrese el primer numero: "))
			b=int(input("ingrese el segundo numero: "))
			if(a>b):
				print("El primer numero es mayor que el segundo")
			elif(a<b):
				print("El segundo numero es mayor que el primero")
			else:
                                print("Son iguales")
			print(op1)
			print(op2)
			print(op3)
			print(op4)
			print(op5)
			print(op6)
			print(op7)
			print(op8)
			print(op9)
			op=int(input("Elija una opción entre 1 y 9: "))
		if (op==6):
			a=int(input("ingrese el primer numero: "))
			b=int(input("ingrese el segundo numero: "))
			if(a%2==0):
				print("El primer numero es par")
			elif(a!=0):
				print("El primer numero es impar")
			if(b%2==0):
				print("El segundo numero es par")
			elif(b!=0):
				print("El segundo numero es impar")
			print(op1)
			print(op2)
			print(op3)
			print(op4)
			print(op5)
			print(op6)
			print(op7)
			print(op8)
			print(op9)
			op=int(input("Elija una opción entre 1 y 9: "))
		if (op==7):
			a=int(input("ingrese el primer numero: "))
			b=int(input("ingrese el segundo numero: "))
			c=int(input("ingrese el tercer numero: "))
			p=(a+b+c)/3
			print("El resultado del promedio es: ",p)
			print(op1)
			print(op2)
			print(op3)
			print(op4)
			print(op5)
			print(op6)
			print(op7)
			print(op8)
			print(op9)
			op=int(input("Elija una opción entre 1 y 9: "))
		if (op==8):
			f=str(input("Ingrese una frase"))
			ca=0
			ce=0
			ci=0
			co=0
			cu=0
			for i in range(0, len(f)):
				if(f[i]=="a" or f[i]=="A"):
					ca+=1
				elif(f[i]=="e" or f[i]=="E"):
					ce+=1
				elif(f[i]=="i" or f[i]=="I"):
					ci+=1
				elif(f[i]=="o" or f[i]=="O"):
					co+=1
				elif(f[i]=="u" or f[i]=="U"):
					cu+=1
			print("Tiene ", ca," letras A")
			print("Tiene ", ce," letras E")
			print("Tiene ", ci," letras I")
			print("Tiene ", co," letras O")
			print("Tiene ", cu," letras U")
			print(op1)
			print(op2)
			print(op3)
			print(op4)
			print(op5)
			print(op6)
			print(op7)
			print(op8)
			print(op9)
			op=int(input("Elija una opción entre 1 y 9: "))
	print("GRACIAS! VUELVA PRONTO!")
