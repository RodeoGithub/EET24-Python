def e10():
    cant=int(input("Ingrese la cantidad de materias: "))
    apr=0
    desapr=0
    ac=0
    for i int range (0,cant):
        nota=int(input("Nota: "))
        ac=ac+nota
        if(nota<6):
            desapr=desapr+1
        else:
            apr=apr+1
    prom=ac/cant
    print("Su promedio es: ",prom)
    print("Aprobo: ",apr)
    print("Desaprobo: ",desapr)
    
