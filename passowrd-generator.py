from random import randint
import os

small_letter = ["a",'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm','n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
Big_letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(','(',')','-','_','+','=','[','{',']','}',';',':','"',',','<','.','>','/',"?",'~','|']

letters = [small_letter , Big_letter , numbers , symbols]

length = 10

password = []

def set_length():
    global length
    length = int(input("Set how many letter should have your password:"))
    
def random_password():
    global length, password
    i = 0
    while i < length: 
        j=-1
        k=-1
        for kategory in letters:
            j+=1
        first_index = int(randint(0,j))
        for kategory in letters[first_index]:
            k+=1
        second_index = int(randint(0,k))
        password.append(letters[first_index][second_index])
        i+=1
          
def clear_password():
    global password
    password = []
    
def print_password():
    global length , password
    password = ''.join(map(str,password))
    print("This is your random generated password: " + password)

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

while True:
    clearConsole()
    set_length()
    clear_password()
    random_password()
    print_password()
    input("Press Enter")
    