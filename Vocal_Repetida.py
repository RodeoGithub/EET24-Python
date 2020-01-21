def e3():
    texto=str(input("Ingrese un texto"))
    a=0
    e=0
    i=0
    o=0
    u=0
    for x in range(0, len(texto)):
        if(texto[x]=='a' or texto[x]=='A'):
            a=a+1
        elif(texto[x]=='e' or texto[x]=='E'):
            e=e+1
        elif(texto[x]=='i' or texto[x]=='I'):
            i=i+1
        elif(texto[x]=='o' or texto[x]=='O'):
            o=o+1
        elif(texto[x]=='u' or texto[x]=='U'):
            u=u+1
    if(a>e and a>i and a>o and a>u):
        print("La vocal más usada es 'A'")
    elif(e>a and e>i and e>o and e>u):
        print("La vocal más usada es 'E'")
    elif(i>a and i>e and i>o and i>u):
        print("La vocal más usada es 'I'")
    elif(o>a and o>e and o>i and o>u):
        print("La vocal más usada es 'O'")
    elif(u>a and u>e and u>i and u>o):
        print("La vocal más usada es 'U'")
    else:
        print("Hay más de una vocal que se repite la mayor cantidad de veces")
    
                
        
