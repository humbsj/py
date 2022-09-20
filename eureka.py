#Funciones

def encuentra(cad,c): #(entrar,t)
    indice = 0
    while indice < len(cad): #6
        if cad[indice] == c:
            return indice
        indice = indice + 1
    return print("no hay n")

#Main

x = input("Coloca valor de cad: ") # entrar
y = input("Coloca valor de c: ") # n

encuentra(x,y)