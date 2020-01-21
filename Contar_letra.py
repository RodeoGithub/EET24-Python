"""
This program shows how many occurrences a character has in a sentence
"""

def e3():
    frase=str(input("Ingrese una frase: "))
    b=str(input("Ingrese el caracter buscado: "))
    c=0
    for i in range (0,len(frase)):
        if(frase[i]==b):
            c=c+1
    print("La letra buscada aparece ", c, " veces")
