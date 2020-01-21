"""
This program shows any number between an initial integer to another integer.
Using "while"
"""

def e6():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    if(a<b):
        minor=a
        major=b
    else:
        major=a
        minor=b
    i=minor
    while(i<=major):
        print(i)
        i=i+1
    
