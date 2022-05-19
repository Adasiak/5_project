from random import randint
import os
import time
# from keyboard import press
# press('enter')
import subprocess

number_of_tries = 0

names = ['Wiktor','Adam','Natalia','Kasia',
         'Piotr','Basia','Marek','Pawel','Dominika',
         'Maja','Monika','Dominik','Andrzej','Maciek',
         'Zuza','Jakub','Jaroslaw','Adrianna','Ada','Leopold']
capital_cities = ['WashingtonDc','Warsaw','Berlin','NewYork','Sydney',
                'Sandiego','Paris','SanFrancisco','Rome','Madrid','London','MexicoCity']
country= ["Poland','France','UnitedStates','Spain','Germany','Italy','Mexico','Australia"]

kategories = [names , country , capital_cities ]

list_of_kategories = ["names",'country','capital cities']

word = ""
helpword=""
user_word = []
used_letter = []

true = True

def random_kategories():
    global word,helpword
    i=-1
    j=-1
    random_or_not = input("Do you want to random generate a category? Y/n:")
    if random_or_not == "n":
        for index, category in enumerate(list_of_kategories):
            print(index + 1, category)
        first_index = int(input("Which kategory do you want to chose:")) - 1
    else:
        for kategory in kategories:
            i+=1
        first_index = int(randint(0,i))
    for category in kategories[first_index]:
        j+=1
    second_index = int(randint(0,j))
    word = kategories[first_index][second_index].lower()
    helpword = kategories[first_index][second_index]
    
    
    
def start_game():
    clearConsole()
    global word , user_word , used_letter , number_of_tries
    number_of_tries = 0
    user_word.clear()
    used_letter.clear()
    for _  in word:
        user_word.append("_")
    print(user_word)

def find_index(word, letter):
    global number_of_tries,found_letter,user_word
    help = 0
    for letterr in word:
        if letterr == letter:
            print("found")
            i=0
            while i < word.count(letter):
                user_word[word.index(letter,word.index(letter)+i)] = letter
                i+=1
            print(user_word)
            help += 1
    if help == 0:
        number_of_tries +=1
        print("Mistake try again, you have", 5-number_of_tries, "tries")
    else:
        print("Good job continue")
        
def found_letters():
    global user_word,word
    for letter in word:
        for l in user_word:
            if l == letter:
                print(l)
            else:
                user_word.append("_")

def clear_statistic():
    global number_of_tries
    number_of_tries = 0
    used_letter = []
    
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def finish_game():
    global true
    clearConsole()
    clear_statistic()
    user_choice_v2 = input("Do you want to Start a game one more time ? Y / n :")
    if user_choice_v2 == "n":
        clearConsole()
        print("See you soon")
        true = False
    elif user_choice_v2 == "Y":
       clearConsole()
    
        

# random_kategories()
# time.sleep(10000)

while true != False:
    random_kategories()
    start_game()
    while number_of_tries < 5:
        user_letter = input("Input letter: ")
        used_letter.append(user_letter)
        print("Used letter:",used_letter)
        find_index(word, user_letter)
        if list(word) == user_word:
            clearConsole()
            print("Congratulation You Win, the word was:",helpword)
            input("Press enter to continue")
            number_of_tries = 6
            
    if number_of_tries == 6:
        finish_game()
    elif number_of_tries == 5:
        print("Game Over!, the word was:",helpword)
        input("Press enter to continue")
        finish_game()
    
        
    

