import os

def clearConsole():
    command = 'cls'
    os.system(command)
    
def print_menu():
    print (" ------------------------------------------------ ")
    print ("|                                                |")
    print ("|    07Menu                                      |")
    print ("|    Name : Aimen Rehan                          |")
    print ("|    Version : 01                                |")
    print ("|                                                |")
    print (" ------------------------------------------------\n ")
    print ('1. Hello World')
    print ('2. Goodbye World')
    print ('3. Goodbye Person')
    print ('4. Good Teacher')
    print ('5. forLoop')
    print ('6. whileLoop')
    print ('7. string Loop')
    print ('8. Convert to ascii')
    print ('9. Encode a string' )
    print ('x. To Exit' )
 
def HelloWorld():
     print('\n----Start of Output ---------------------------')
     print('\nHello World')
     print('\n----End of Output -----------------------------')
     input('\n\n\nPress enter to continue ')

def GoodbyeWorld():
     print('----Start of Output ---------------------------\n')
     print('Hello World')    
     input('------> Program paused - press enter to continue')
     print('Goodbye World')
     print('\n----End of Output -----------------------------')
     input('\n\n\nPress enter to continue ')
  
def GoodbyePerson():
    print('----Start of Output ---------------------------\n')
    print ('Hello')    
    name = input('What is your name ?')
    print('Goodbye ' + name)
    print('\n----End of Output -----------------------------')
    input('\n\n\nPress enter to continue')

def GoodTeacher():
    print('----Start of Output ---------------------------\n')
    tname = input("Teacher's name (try Mr Horan) ")
    if tname =="Mr Horan":
     print("You ar lucky, he is a great teacher")
    else:
     print (tname + " is an ok teacher")
    print('\n----End of Output -----------------------------')
    input('\n\n\nPress enter to continue')

def forLoop():
    print('----Start of Output ---------------------------\n')
    for numbers in range(1, 500): 
       print(numbers) 
    print('\n----End of Output -----------------------------')
    input('\n\n\nPress enter to continue')

def whileLoop():
    print('----Start of Output ---------------------------\n')
    subject = input("What is the name of this subject ")
    while subject != "IST":
        print("Not Correct - try again")
        subject = input("What is the name of this subject ")
    if subject == "IST":
        print ("\n\nCongratulations!!\n\n")
    print('\n----End of Output -----------------------------')
    input('\n\n\nPress enter to continue')

def ToExit():
    print('----Start of Output ---------------------------\n')
    print('\n----End of Output -----------------------------')
    input('\n\n\nPress enter to continue')

if __name__=='__main__':
    while(True):
        print_menu()
        option = (input('Enter an option '))
        if option == '1':
            HelloWorld()
            clearConsole()
        elif option == '2':
            GoodbyeWorld()
            clearConsole()
        elif option == '3':
            GoodbyePerson()
            clearConsole()
        elif option == '4':
            GoodTeacher()
            clearConsole()
        elif option == '5':
            forLoop() 
            clearConsole()
        elif option == '6':
            whileLoop()
            clearConsole()
        elif option == 'x' :
            ToExit()
            break
        else:
          print('----Start of Output ---------------------------')
          print('\ninvalid option\n')
          print('----End of Output -----------------------------')
          input('\n\n\nPress enter to continue ')
          clearConsole()