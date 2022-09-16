
#FUNCTIONS

def estaentre(x,y,z):
    int (x)
    int (y)
    int (z)

    if(y<=x<=z):
        a=1
        return print(a)
    else:
        b=0
        return print(b)

def message():
    x = input("Coloca valor de x: ")
    y = input("Coloca valor de y: ")
    z = input("Coloca valor de z: ")
    estaentre(x,y,z)

def v(x,y,z):
    if(x>0 and y>0 and z>0 
    and type(x) == type(1)
    and type(y) == type(1)
    and type(z) == type(1)):
        print("d")
    else:
        print("Tiene que ser un numero y positivo")

#MAIN

x = input("Coloca valor de x: ")
y = input("Coloca valor de y: ")
z = input("Coloca valor de z: ")
#print(type(x))
#estaentre(x,y,z)
v(x,y,z)