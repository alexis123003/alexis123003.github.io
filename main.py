yogurt = 1.00
tomato = 0.50
lettuce = 0.25
skittles = 0.75

print("1. Yogurt ($1.00)")
print("2. Tomato ($0.50)")
print("3. Lettuce ($0.25)")
print("4. Skittles ($0.75)")

first_topping = int(input("Please Enter the First topping with numbers above (1-4): "))
second_topping = int(input("Please Enter the Second topping with numbers above (1-4): "))
third_topping = int(input("Please Enter the Third topping with numbers above (1-4): "))

# numbers to prices
prices = {1: yogurt, 2: tomato, 3: lettuce, 4: skittles}
topping_total = prices[first_topping] + prices[second_topping] + prices[third_topping]

if (topping_total >= 1):
    discount = topping_total * 0.10
    print(f"You have a 10% discount Your total is ${topping_total - discount:.2f}")
else:
    print(f"Your total is ${topping_total:.2f}")