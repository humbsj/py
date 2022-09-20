#Funciones

def encuentra(cad,c): #(entrar,t)
    indice = 0
    while indice < len(cad): #6
        if cad[indice] == c:
            return print("La letra"+ " "+ str(y)+ " "+ "se encuentra en la posición" + 
            " " + str(indice+1))  
            #aquí me indica el índice de la letra 
            #es necesario sumar 1 al indice xq se cuenta
            #desde el 0.
        indice = indice + 1
    return print("no hay n")

#Main

x = input("Coloca valor de cad: ") # entrar
y = input("Coloca valor de c: ") # t

encuentra(x,y)