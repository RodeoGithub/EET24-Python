"""
This program shows any number between an initial integer to another integer.
"""
def e6():
    a=int(input("Enter a number: "))
    b=int(input("Enter a numer: "))
    if(a<b):
        minor=a
        major=b
    else:
        major=a
        minor=b
    for i in range (minor,major+1):
        print(i)
    
