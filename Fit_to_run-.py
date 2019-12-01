"""
This program check if a person is fit to run a race. Following preset rules
"""

def ej5():
    gen=input("Enter your gender  (Male o Female): ")
    age=int(input("Enter your age: "))
    print("Enter the time taken in your last race:")
    h=int(input("Hs: "))
    m=int(input("Min: "))
    s=int(input("Seg: "))
    carrera=(h*60)+m+(s/60)
    if(gen=='Male'):
        if(age<40):
            if(carrera<150):
                print("Fit to run")
            else:
                print("not suitable to run")
        else:
            if(carrera<175):
                print("Fit to run")
            else:
                print("not suitable to run")
    else:
        if(age<30):
            if(carrera<180):
                print("Fit to run")
            else:
                print("not suitable to run")
        else:
            if(carrera<200):
                print("Fit to run")
            else:
                print("not suitable to run")






        
    
