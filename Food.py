#ask from user for three fav food items and store them in list and print ""You like these food items: " followed by the list of food items
food_items = []
for i in range(3):
    food = input("Enter your favorite food item: ")
    food_items.append(food)
print("You like these food items: ", food_items) 