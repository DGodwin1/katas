#make a string uppercase.
def make_string_upper_case(my_string):
    print my_string.upper()

#making string lowercase
def make_a_string_lower_case(string):
    print string.lower()

#now want to check the case of a string
def check_case_of_string(a):
    print "Entered %s" % a
    print "We're going to check the case"
    if (a.isupper()):
        print "%s is uppercase." % a
        maybe_change_string_case(a)
    elif (a.islower()):
        print "%s is lowercase." % a
        maybe_change_string_case(a)

def maybe_change_string_case(something):
    print "How would you like to proceed?"
    b = raw_input("1 = I'd like it uppercase. 2 = I'd like it lowercase\n >> ")
    if b == "1":
        make_string_upper_case(something)
    elif b == "2":
        make_a_string_lower_case(something)
    else:
        print "Try again. That didn't work. Make sure you type either 1 or 2"
        maybe_change_string_case(something)


make_string_upper_case("AbCCc")

make_a_string_lower_case("HELLO")

check_case_of_string("hello")
