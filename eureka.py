#Funciones

def encuentra(cad,c,i): #(entrar,t)
    indice = int(i)
    while indice < len(cad): #6
        if cad[indice] == c:
            return print("La letra"+ " "+ str(y)+ " "+ "se encuentra en la posición" + 
            " " + str(indice+1))  
            #aquí me indica el índice de la letra 
            #es necesario sumar 1 al indice xq se cuenta
            #desde el 0.
        indice = indice + 1
    return print("La letra" + " " + str(x) + " "+ "no está en la cadena")

#Main

x = input("Coloca valor de cad: ") # entrar
y = input("Coloca valor de c: ") # t
z = input("Coloca el índice desde donde quieres buscar:")

encuentra(x,y,z)