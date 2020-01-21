"""
This program shows the total sum from a integer to another integer
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
    for i in range (minor,major+1):
        total=total+i
    print("Total sum: ",total)
    
