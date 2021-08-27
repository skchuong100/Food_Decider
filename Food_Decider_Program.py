#Import the random file 
import random

#Create list of restaurants for each area in SoCal
def preexisting_list():
  #Ask which location does the user want
  location_picker = input("Which location do you want a list of?: ")
  
  #Create an if statement if the user wants a list from Fountain Valley
  if location_picker == "Fountain Valley" or location_picker == "FV":
    return FV()

  #Create an if statement if the user wants a list from Westminster
  elif location_picker == "Westminster":
    return Westminster()

  #Create an if statement if the user wants a list from Garden Grove  
  elif location_picker == "Garden Grove" or location_picker == "GG":
    return Garden_Grove()

  #Create an if statement if the user wants a list from Santa Ana
  elif location_picker == "Santa Ana" or location_picker == "SA":
    return Santa_Ana()

  #Create an if statement if the user wants a list from Irvine
  elif location_picker == "Irvine":
    return Irvine()

  #Create an if statement if the user wants a list from Tirrance 
  elif location_picker == "Torrance":
    return Torrance()

  #Create an if statement if the user wants a list from Los Angeles
  elif location_picker == "Los Angeles" or location_picker == "LA":
    return LA()

  #Create an if statement if the user wants a list from Huntington Beach
  elif location_picker == "Huntington Beach" or location_picker == "HB":
    return Huntington_Beach()

  #Create an if statement if the user wants a list from Irvine
  elif location_picker == "Irvine":
    return Irvine()  


def Torrance():
  #Create list for Torrance
  Torrance_list = ["Kagura", "Bowl Thai", "Torimatsu", 
  "Azuma", "On + On Kitchen", "Boiling Point"]
  return Torrance_list

def Huntington_Beach():
  #Create list for Hubntington Beach
  HB_List = ["Sushi On Fire", "Duke's Huntington Beach", "Charlie's Gyros", 
  "Blue Gold", "Nori Poke Sushi"]
  return HB_List
  
def Irvine():
  #Create list for Irvine 
  Irvine_list = ["House of ShabuShabu", "Curry House CoCo Ichibanya", 
  "Krave Asian Fusion", "Kebab Shop", "Kura Sushi"]
  return Irvine_list

def Santa_Ana():
  #Create list for Santa Ana
  SA_list = ["Whealthy", "Kaizen Shabu", "The Block",
  "AYCE Sushi SCM", "Koco Sushi"]
  return SA_list

def Garden_Grove():
  #Create list for Garden Grove
  GG_List = ["Mochinut", "Shawarma House", "Hodori Snack", "Duck Donuts", 
  "Cafe Orange", "Red Castle", "Star BBQ", "Boiling Point", "Rodeo 39"]
  return GG_List

def Westminster():
  #Create list for Westminster
  Westminter_list = ["Grinkgo Katsu", "Silverlake Ramen", 
  "SoCal Wings", "Chungchun Rice Hotdog"]
  return Westminter_list

def FV():
  #Create list for Fountain Valley
  Fv_list = ["Ikram Grill", "Hot-Off-the-Gril", "Vox Kitchen", "Kensho", "Nep Cafe", "Red Flame", 
  "Sabrosada", "Taco Bell", "Project Poke", "Full Moon", "Nikado", "Dennys"]
  return Fv_list

def LA():
  #Create list for Los Angeles
  LA_list = ["Perch", "Hayoto", "Marugame Monzo", 
  "Chinchikurin", "PASTA e PASTA by Allegro"]
  return LA_list

#Create a function that will choose which place based on a random number chosen
def food_decider1(list1):
  random_num = random.randrange(0, (len(list1)))
  print()
  print("Go here:", list1[random_num])
  print("Have a good day!")

def main():
  #Create an empty list
  Food_list = []
  #Create a variable
  i = 0
  print("Hello! I will help you decide places to go since you can not decide! (Orange and Los Angeles County Edition")
  print()
  option1 = input("Do you want a preexisting list of foods or do you want to create a list? Enter Preexisting or New List: ")
  
  #Create an if statement if the user wants a preexisting list
  if option1 == 'Preexisting':
    Food_list = preexisting_list()
    
  else:
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
  question2 = input("Is the food you are craving on the list? \nEnter Yes or No: ")
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

  elif question2 == "No":
    food_decider1(Food_list)
    #Create an else statement is the list has nothing of what the user craves

#Call the main function
main()
