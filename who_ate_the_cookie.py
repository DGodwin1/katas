#https://www.codewars.com/kata/who-ate-the-cookie
def cookie(a):
    if type(a) == str:
        return(the_actual_message("Zach"))

    elif type(a) == int or type(a) == float:
        return(the_actual_message("Monica"))

    else:
        return(the_actual_message("the dog"))

def the_actual_message(name_of_person):
    return("Who ate the last cookie? It was {}!").format(name_of_person)
  
print(cookie("s"))
#should return Zack
print(cookie(10+1))
# should return Monica
print(cookie(-111.5))
#should return Monica
print(cookie(True))
#should return dog
