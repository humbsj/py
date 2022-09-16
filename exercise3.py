
#FUNCTIONS

def estaentre(x,y,z):
    if(y<=x<=z):
        a=1
        return print(a)
    else:
        b=0
        return print(b)

#MAIN

x = int(input("Coloca valor de x: "))
y = int(input("Coloca valor de y: "))
z = int(input("Coloca valor de z: "))
estaentre(x,y,z)