
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
    v(x,y,z)

def v(x,y,z):
    #if(type(int(x)) == type(1)
    #and type(int(y)) == type(1)
    #and type(int(z)) == type(1)):
    #    print("d")
    
    #else:
    #    if(int(x)>0 and int(y)>0 and int(z)>0)
    #    print("Tiene que ser un numero")
    while (int(x)>0 and int(y)>0 and int(z)>0):
    #and type(int(x)) == type(1) and type(int(y)) == type(1)
    #and type(int(z)) == type(1) ):
        estaentre(x,y,z)
        break;
    else:
        #if(type(x) == type(1) and type(y) == type(1)
    #and type(z) == type(1)):
            print("Debe ser positivo y no puede ser 0")
            message()

#MAIN

x = input("Coloca valor de x: ")
y = input("Coloca valor de y: ")
z = input("Coloca valor de z: ")
#print(type(x))
#estaentre(x,y,z)
v(x,y,z)