#Funciones

def countletra(x, letra, z): #(Gala, a)
    #char = x #Gala # no es necesaria esta línea, ya que
    #este valor char solo almacena el siguiente caracter de
    #la cadena en el bucle. 
    s = int(z)
    count = 0 
    for char in x[s:]: #Gala
        if char == letra: #a
            count = count + 1
    print("la letra" + " "+ str(y) + " "+ "se encuentra" +" "+ str(count)+ " veces.")

#main

x = input("escribe palabra: ")
y = input("escribe la letra que quieres contar: ")
z= input("Escoge desde qué posición contar: ")
countletra(x, y, z)