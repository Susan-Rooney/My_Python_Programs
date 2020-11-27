import pyinputplus as pyip

cost = {"wheat": 0.5, "white": 0.5, "sourdough": 1,
         "chicken": 1, "turkey": 1, "ham": 0.5, "tofu": 1,
         "cheddar": 1, "Swiss": 1, "mozzarella": 1.5,
         "mayo": 0.25, "mustard": 0.10, "lettuce": 0.10, "tomato": 0.25}

print("what type of bread would you like?")
bread_type = pyip.inputMenu(["wheat", "white", "sourdough"], numbered=True)
print("you have chosen " + bread_type + " bread.")

print("What type of protein would you like?")
protein_type = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], numbered=True)
print("you have chosen " + protein_type + ".")

print("Your sandwich now has " + bread_type + " bread and " + protein_type + ".")

print("Do you want cheese? ")
response = pyip.inputYesNo()
if response == "Yes" or "yes" or "y":
    print("What type of cheese would you like?")
    cheese_type = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"], numbered=True)
else:
    cheese_type = "no cheese"    

print("Your sandwich now has " + bread_type + " bread and " + protein_type + " and " + cheese_type + ".")

print("Would you like a condiment?")
response = pyip.inputYesNo()
if response == "yes":
    condiment = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'], numbered=True)
else:
    condiment = "no condiment"
print("You have chosen " + condiment + ".")

print("Your sandwich will be made with " + bread_type + " bread, " + protein_type + ", " + cheese_type + ", and " + condiment + ".")

print("How many sandwiches would you like?")
no_of_sandwiches = pyip.inputInt(min=1)

sandwich_cost = no_of_sandwiches * (cost[bread_type] + cost[protein_type]+ cost[cheese_type] + cost[condiment])
print("Your amount due is: " + str(sandwich_cost))