# 1 . a
# 2 . a
# 3 . c
# 4 . a
# 5 . a
# 6 . a
# 7 . a
# 8 . c
# 9 . b


# 10. POST, GET, PUT, PATCH, and DELETE.

# 11. 
# Adventage of SOAP
# * Language, platform, and transport independent (REST requires use of HTTP)     
# * Works well in distributed enterprise environments (REST assumes direct point-to-point communication)
# * Standardized
# * Provides significant pre-build extensibility in the form of the WS* standards
# * Built-in error handling
# * Automation when used with certain language products

# Adventage of REST
# * Uses easy to understand standards like swagger and OpenAPI Specification 3.0
# * Smaller learning curve
# * Efficient (SOAP uses XML for all messages, REST mostly uses smaller message formats like JSON)
# * Fast
# * Closer to other Web technologies in design philosophy

# 12.
# 
def prime_numbers():    # Declare the variables
    a, b, i, j, flag = 0, 0, 0, 0, 0

    a = 0
     
    # Ask user to enter value of interval
    print("Enter upper bound of the interval:",
                                      end = "")
    b = int(input()) # Take input
    print(b)
     
    # Print display message
    print("Prime numbers between", a, "and",
                        b, "are:", end = "")
 
    # Traverse each number in the interval
    # with the help of for loop
    for i in range(a, b + 1):
 
        # Skip 1 as1 is neither
        # prime nor composite
        if (i == 1 or i == 0):
            continue
 
        # flag variable to tell
        # if i is prime or not
        flag = 1
         
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                flag = 0
                break
             
        # flag = 1 means i is prime
        # and flag = 0 means i is not prime
        if (flag == 1):
            print(i, end = " ") 


# 13 
import json
from datetime import datetime 

def jsonnn(path):
 
    f = open(path)

    data = json.load(f)

    list_of_date_birth = []
    for emploee in data["employees"]:
        list_of_date_birth.append(datetime.strptime(emploee["date_of_birth"], '%d-%m-%Y'))

    list_of_date_birth.sort()
    
    oldest_employ_date_of_birth = list_of_date_birth[0]

    for emploee in data["employees"]:
        if datetime.strptime(emploee["date_of_birth"], '%d-%m-%Y') == oldest_employ_date_of_birth:
            print("the oldest employee is:",emploee["name"], emploee["surname"] )
   
if __name__ == '__main__':
    print("Task 12")
    prime_numbers()
    print()
    print("Task 13")
    path_to_json_file = "/Users/apple/Desktop/Programowanie/database.json"
    jsonnn(path_to_json_file)
    