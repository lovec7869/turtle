#Write a program that calculates the total amount of a meal purchased at a resturant
#June 19, 2020
#CTI-110 P2HW1 - Meal Tip Tax Calculator
#Carlando Love
#

#Ask user to enter the charge for food amount
foodCharge = float(input("Enter the meal's charge: "))

#Ask user to enter the tip amount
tipAmount = float(input("Enter the tip percentage (in decimal form): "))

#Ask the user to enter the state tax
stateTax = float(input("Enter the state tax (in decimal form): "))

#Calculate tip
calculateTip = foodCharge * tipAmount

#Calculate tax
calculateTax = foodCharge * stateTax

#Calculate total cost
totalCost = foodCharge + calculateTip + calculateTax

#Display the meal amout
print ("Meal: $", format(foodCharge, ",.2f"))

#Display the tip
print ("tip: $", format (calculateTip, ",.2f"))

#Display the tax
print ("tax: $", format(calculateTax, ",.2f"))

#Display the total cost
print ("total cost: $", format(totalCost, ",.2f"))

