# Define an empty list to store the favorite food items
fav_food = []

# Ask the user how many items they want to enter
num_items = int(input("How many items do you want to enter? "))

# Loop through the number of items
for i in range(num_items):
    # Ask the user for each item and append it to the list
    item = input("Enter item " + str(i+1) + ": ")
    fav_food.append(item)

# Print the list of favorite food items
print("Your favorite food items are: ")
print(fav_food)

# Define the file name and path on the desktop
file_name = "fav_food.txt"
file_path = "C:\\Users\\Public\\Desktop\\" + file_name

# Open the file in write mode
file = open(file_path, "w")

# Write each item in the list to the file, separated by a newline
for item in fav_food:
    file.write(item + "\n")

# Close the file
file.close()

# Print a confirmation message
print("The list has been stored in the file " + file_name + " on the desktop")
