#number = str(1+1)
#txt_welcome= ("Hi there, I am a program written in python :D")
#message = number+(" ")+txt_welcome
#print (message)
#message_type=type(message) 

#FUNCTION DECLARATION
#def welcome_message(number,message):
#   txt= str(number)+(" ")+message
#   print(txt)

#welcome_message(1,"hi there, I am the first function of Humberto :D")

def doyouneedmore(dyn):
        if(dyn == "Y"):
            input_n = int(input("Choose how many times the message will appear: "))
            validation(input_n)
            input_cn = input("Do you need more? (Y/N): ")
            doyouneedmore(input_cn)
        elif(dyn == "N"):
            print("Thanks for using this simple programm")

def error():
    print("The number must be >0...")
    #int(input("Choose how many times the message will appear:"))
    input_n = int(input("Choose how many times the message will appear: "))
    validation(input_n)
    
        
def count(n):
    while (n>0):
        print(n)
        count(n-1)
        break;     
    else:      
        print("Hi, This is the first time i am using recursive programming stuff in python")
        
def validation(inp):
    if (inp>0):
        count(inp)
    else:
        error()

##MAIN

input_n = int(input("Choose how many times the message will appear: "))
validation(input_n)
input_c = input("Do you need more? (Y/N): ")
doyouneedmore(input_c)