#Import the random file 
import random
#Create a function that will choose which place based on a random number chosen
def food_decider1(list1):
  random_num = random.randint(0, (len(list1))+1)
  print()
  print("Go here:", list1[random_num])
  print("Have a good day!")

def main():
  #Create an empty list
  Food_list = []
  #Create a variable
  i = 0
  print("Hello! I will help you decide places to go since you can not decide!")
  print()
  #Ask the user to input how many places they can't choose 
  num_inputs = int(input("Please enter the number of places you can not decide on: "))
  #Create a loop that will loop as many times as what number was inputted
  while i < num_inputs:
    #Ask the user to input the name of the place
    food_name = input("Enter the name of the place: ")
    #Add it to the list
    Food_list.append(food_name)
    i+=1
  print()
  #Display the list of places entered
  print("List of places:", Food_list)
  print()
  #Get specific by asking if the user is craving any type of food
  question2 = input("Is the food/drink you are craving on the list? \nEnter Yes, No, or Anything (if you are fine with anything): ")
  #Create an empty list
  specific_list = []
  #Create a variable
  k = 0
  #Create an if statement if the user is craving something
  if question2 == 'Yes':
    #Ask the user what thery crave
    num_of_food_craves = int(input("How many places from what you inputted sells what you crave?: "))
    print()
    #Create a while loop that will loop as many times as the number inputted
    while k < num_of_food_craves:
      #Have the user input what they are craving
      food_finder = input("What is the name(s) of the place(s)?: ")
      #Add the name to the list
      specific_list.append(food_finder)
      #Add one to the variable
      k+=1
    #Add the list as an arguement to the call of the function
    food_decider1(specific_list)
  #Create an elif statement if the user is craving anything
  elif question2 == "Anything":
    #Add the list as an argument to the call of the function
    food_decider1(Food_list)
  #Create an else statement is the list has nothing of what the user craves
  else:
    print()
    print("Try Again")
#Call the main function
main()
