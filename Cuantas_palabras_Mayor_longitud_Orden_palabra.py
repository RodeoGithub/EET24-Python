def c3():
    frase=str(input("Ingrese una frase: "))
    max_letras=99999999
    cant_pal=1
    for i in range(0,len(frase)+1):
        pal=''
        while(frase[i]!=" " and i<len(frase)-1 and frase[i]!="."):
            pal=pal+frase[i]
            i=i+1
        if(len(pal)>max_letras):
            max_letras=len(pal)
            n_pal=len(pal)
        cant_pal=cant_pal+1
    print("La cantidad de palabras es: ",cant_pal)
    print("La palabra de mayor longitud es la numero: ",n_pal)
    print("Y esa palabra es: ", pal)
            
