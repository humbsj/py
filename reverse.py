#FUNCIONES

def reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i=0
    j= len(word2)-1

    while j>0:
        print (i,j)
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return print(True)

#MAIN

x=input("Pon palabra 1: ")
y=input("Pon palabra 2: ")
reverse(x,y)