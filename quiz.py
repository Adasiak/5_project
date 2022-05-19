import json
from random import randint
import random
import os 

points = 0
# used_question = set()
used_question = []

def end():
    clearConsole()
    print("Thanks for game!")
    exit()

def show_questions(questions):
    global points
    print()
    print(questions["pytanie"])
    print("a",questions["a"])
    print("b",questions["b"])
    print("c",questions["c"])
    print("d",questions["d"])
    print()
    
    i = 0
    while i != 1:
        abcd = {"a",'b','c','d'}
        answear = input("Która odpowiedz jest prawdziwa: ")
        if answear in abcd:
            print()
            i = 1
            if answear == questions["prawidłowa_odpowiedz"]:
                points +=1
                print("Good job")
            else:
                print("Try one more time, this time mistake, right answear is:",questions["prawidłowa_odpowiedz"])
        elif answear == "n":
            end()
        else:
            print("Wrong format try again")
    
def clear_statistic():
    global points 
    points = 0
    

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
    
def load_question_from_file():
    global used_question   
    with open("quiz.json") as json_file:
        questions = json.load(json_file)
        # create list of that much elements how long is questions 
        l = list(range(len(questions)))
        # create new list of value from list l but in random order
        lr = random.sample(l, len(l))   
        show = 0     
        for i in range(0,len(questions)):
            if len(questions)==len(used_question):
                answear = input("You have all of question in base.\n Would you like to answear for them one more time? Y / n :")
                if answear == "n":
                    end()
                
                else:
                    used_question.clear()
                    print("Now you can ansewar for the same question again. Good luck!\n")
                    
            if questions[lr[i]] not in used_question:
                used_question.append(questions[lr[i]])
                show_questions(questions[lr[i]])
                show +=1
                if show >= 3:
                    break

while True:
    clearConsole()
    clear_statistic()
    load_question_from_file()
    print()
    print("Koniec Gry uzyskałeś:" , points ,"punktów")
    answear = input("Press Enter to continue, Exit press n")
    if answear == "n":
        end()
