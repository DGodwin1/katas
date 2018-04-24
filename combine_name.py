#https://www.codewars.com/kata/grasshopper-combine-strings/train/python
def combine_names(first_name, second_name):
    print "%s %s" % (first_name, second_name)

#test cases from Codewars
combine_names("James", "Stevens")
combine_names("Davy", "Black")
combine_names("Arthur", "Dent")

#users should be able to type their own details and we process that
def user_enters_own_name():
    print "Hi there, what's your first name?"
    first_name_input = raw_input("> ")
    print "And your second name?"
    second_name_input = raw_input("> ")
    print "%s %s" % (first_name_input, second_name_input)

user_enters_own_name()
