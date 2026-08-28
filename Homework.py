print("Name: Alexis Beer")
print("Address: 47 N Prospect, Reveille Illinois")
print("Phone number: 217-898-0858")
print("College Major: Computer Science")
#2

total_sales = input("Enter the projected amount of total sales: $")
total_sales = int(total_sales)
profit_percentage = 0.23
#process
profit = total_sales * profit_percentage
#Output
print(f"The projected profit from ${total_sales:.2f} in total sales is ${profit:.2f}")


#3
square_ft = input("Enter the total number of square feet in a tract of land")
square_ft = int(square_ft)
acres =  43560 
#process
total = float(square_ft/acres)
#Output
print(f"The total acres from {square_ft:.2f} is {total:.2f} acres")