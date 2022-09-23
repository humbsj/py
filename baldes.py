#FUNCION

def enbalde(lista, min, max):
    count = 0
    for i in lista:
        if min < i < max:
            count = count + 1
    print(count)

def calcular(numbaldes): # ejm: numbaldes = 8
    baldes = [0] * numbaldes # [0,0,0,0,0,0,0,0]
    anchobalde = 1.0 / numbaldes # 1/8 # 0.125 partes

#Hasta aquí se define el ancho del balde

    for i in range(numbaldes): # rango: 0,1,2,3,4,5,6,7
        min = i * anchobalde    # 0*0,     1*0.125,     2*0.125,     3*0.125,     4*0.125,   5*0.125,      6*0.125,      7*0.125
        max = min + anchobalde  # 0+0.125, 0.125+0.125, 0.250+0.125, 0.375+0.125, 0.5+0.125, 0.625+0.125,  0.75+0.125,   0.875+0.125
        baldes[i] = enbalde(range(1000), min, max)
        #print(min, " hasta ", max) #(0 hasta 0.125)  (0.125 hasta 0.25)  (0.25 hasta 0.375)  (0.375 hasta 0.5) (0.5 hasta 0.625)
    print(baldes)

#MAIN

x = int(input("Ingresa numero de baldes: "))
#lista = input("Coloca cantidad de valores en lista: ")
calcular(x)
#enbalde([0.0,0.1,0.2,0.4,0.7], 0.0, 0.5)
#[]
#enbalde([0.0, 0.25, 0.5, 0.75, 1.0], 0.0, 0.25)