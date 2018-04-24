#https://www.codewars.com/kata/jennys-secret-message/train/python

def greet(name):
    if name == "Johnny":
        print "Hello, my love!"
    else:
        print "Hello, %s!" % name

greet(raw_input("Please enter your username > "))
