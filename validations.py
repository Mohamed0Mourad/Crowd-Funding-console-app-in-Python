#import regex module
import re
#import json library
import json
#file that contains registered users
UsersFile = 'users.json'


def input_validation(msg,start=0,end=None):
    while True:
        inp=input(msg)
        if not inp.isdecimal():
            print("❌Invalid input, Try again!")
        elif start is not None and end is not None:
            if int(inp) in range(start,end+1):
                return int(inp)
            else:
                print("❌Invalid Range. Try Again!")
        else:
            return int(inp)    
        
        
#phone number validation
def phoneNumberValidation(phone):
    return re.match(r'^(010|011|012|015)\d{8}$',phone)
#emailvalidation
def emailvalidate(email):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",email)
    
#get all users registered 
def load_users():
    try:
        with open(UsersFile, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {} #if not found create it and return {} in it 
    

#Save users in users file
def save_users(users):
    with open(UsersFile,'w') as f:
        json.dump(users,f,indent=4)
        
