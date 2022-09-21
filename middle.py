#Functions

def middle(lista):
    #lista = [x,y,z,v]
    del lista[0:4:3] #esto borra entre 0 y 4 
    #tomando espacios de 3
    print(lista)

#main

x = input("Pon valor a: ")
y = input("Pon valor y: ")
z = input("Pon valor z: ")
v = input("Pon valor v: ")
l = [x,y,z,v]
middle(l) 