def e10():
    cant=int(input("Ingrese la cantidad de materias: "))
    apr=0
    desapr=0
    ac=0
    i=0
    while(i<cant):
        nota=int(input("Nota: "))
        ac=ac+nota
        if(nota<6):
            desapr=desapr+1
        else:
            apr=apr+1
        i=i+1
    prom=ac/cant
    print("Su promedio es: ",prom)
    print("Aprobo: ",apr)
    print("Desaprobo: ",desapr)
    
