import math

#Function declaration

def distance (x1, y1, x2, y2):
    diffx=x2-x1
    diffy=y2-y1
    
    diffsqrt = diffx ** 2 + diffy ** 2
    r= math.sqrt(diffsqrt)
    print(r)

def doyouneedmore(dyn):
        if(dyn == "Y"):
            x1i = int(input("ingrese numero x1:"))
            y1i = int(input("ingrese numero y1:"))
            x2i = int(input("ingrese numero x2:"))
            y2i = int(input("ingrese numero y2:"))
            validation(x1i,y1i,x2i,y2i)

            input_cn = input("Do you need more? (Y/N): ")
            doyouneedmore(input_cn)

        elif(dyn == "N"):
            print("Thanks for using this simple programm")

def error():
    print("Valor debe ser mayor a 0")
    x1i = int(input("ingrese numero x1:"))
    y1i = int(input("ingrese numero y1:"))
    x2i = int(input("ingrese numero x2:"))
    y2i = int(input("ingrese numero y2:"))
    validation(x1i,y1i,x2i,y2i)
    #no es necesario doyouneedmore(). 
    #Al terminar la función "validation" no existe un valor para el parámetro que pide doyouneedmore(). Es por eso que el error indica que falta un "dyn"

def validation (x1, y1, x2, y2):
        if(x1>0 and y1>0 and x2>0 and y2>0):
            distance(x1, y1, x2, y2)
        else:
            error()

#MAIN

x1i = int(input("ingrese numero x1:"))
y1i = int(input("ingrese numero y1:"))
x2i = int(input("ingrese numero x2:"))
y2i = int(input("ingrese numero y2:"))
validation(x1i,y1i,x2i,y2i)
input_c = input("Do you need more? (Y/N): ")
doyouneedmore(input_c)