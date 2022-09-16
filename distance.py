import math

#Function declaration

def distance (x1, y1, x2, y2):
    diffx=x2-x1
    diffy=y2-y1
    
    diffsqrt = diffx ** 2 + diffy ** 2
    r= math.sqrt(diffsqrt)
    print(r)

def message():
    x1i = int(input("ingrese numero x1:"))
    y1i = int(input("ingrese numero y1:"))
    x2i = int(input("ingrese numero x2:"))
    y2i = int(input("ingrese numero y2:"))
    validation_positive(x1i,y1i,x2i,y2i)

def doyouneedmore(dyn):
    if(dyn == "Y"):
        #x1i = int(input("ingrese numero x1:"))
        #y1i = int(input("ingrese numero y1:"))
        #x2i = int(input("ingrese numero x2:"))
        #y2i = int(input("ingrese numero y2:"))
        #validation_positive(x1i,y1i,x2i,y2i)
        message()
        input_cn = input("Do you need more? (Y/N): ")
        doyouneedmore(input_cn)

    elif(dyn == "N"):
        print("Thanks for using this simple programm")


def errornegative():
    print("Valor debe ser mayor a 0")
    message()
    #x1i = int(input("ingrese numero x1:"))
    #y1i = int(input("ingrese numero y1:"))
    #x2i = int(input("ingrese numero x2:"))
    #y2i = int(input("ingrese numero y2:"))
    #validation_positive(x1i,y1i,x2i,y2i)
    #no es necesario doyouneedmore(). 
    #Al terminar la función "validation" no existe un valor para el 
    #parámetro que pide doyouneedmore(). 
    #Es por eso que el error indica que falta un "dyn"

def validation_positive (x1, y1, x2, y2):
    if(x1>0 and y1>0 and x2>0 and y2>0 and 
    type(x1) == type(1)and type(y1) == type(1)
    and type(x2) == type(1)and type(y2) == type(1)):
        distance(x1, y1, x2, y2)
    else:
        errornegative()

#def validation_type (x1, y1, x2, y2):
#    if(type(x1) == type(1)and type(y1) == type(1)
#    and type(x2) == type(1)and type(y2) == type(1)):


#MAIN

x1i = int(input("ingrese numero x1:"))
y1i = int(input("ingrese numero y1:"))
x2i = int(input("ingrese numero x2:"))
y2i = int(input("ingrese numero y2:"))
validation_positive(x1i,y1i,x2i,y2i)
input_c = input("Do you need more? (Y/N): ")
doyouneedmore(input_c)