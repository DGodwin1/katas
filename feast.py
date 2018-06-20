#https://www.codewars.com/kata/the-feast-of-many-beasts
def feast(animal_name, dish_name):
  #make into lists so we can compare list positions
  a = list(animal_name)
  b = list(dish_name)
  return(a[0] == b[0]) and (a[-1] == b[-1]))
  
#should return true
print(feast("great blue heron", "garlic naan"))

#should return true
print(feast("chickadee", "chocolate cake"))

#should return false
print(feast("zebra", "curry"))
