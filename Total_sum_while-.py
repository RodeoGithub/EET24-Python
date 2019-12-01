"""
This program shows the total sum from a integer to another integer using "while"
"""
def e7():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    if(a<b):
        minor=a
        major=b
    else:
        major=a
        minor=b
    total=0
    i=minor
    while(i<=major):
        total=total+i
        i=i+1
    print("Total sum: ", total)
    
