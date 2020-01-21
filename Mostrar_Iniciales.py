def e2():
        frase=str(input("Ingrese una frase: "))
        pal=1
        for i in range (0,len(frase)):
                if(pal):
                        print(frase[i])
                        pal=0
                elif(frase[i]==" "):
                        pal=1
