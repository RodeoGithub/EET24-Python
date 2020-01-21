"""
This program count and shows the number of vowels in a sentence.
"""

def e2():
    texto=str(input("Ingrese el texto: "))
    cv=0
    for i in range (0, len(texto)):
        if(texto[i]=='a' or texto[i]=='i' or
           texto[i]=='e' or texto[i]=='o' or
           texto[i]=='u' or texto[i]=='A' or
           texto[i]=='I' or texto[i]=='E' or
           texto[i]=='O' or texto[i]=='U'):
            cv=cv+1
    print("La cantidad de vocales es: ", cv)

