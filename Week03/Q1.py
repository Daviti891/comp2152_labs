print("="*50)
print("Question 1: Student Grade List")
print("="*50)

grade=[85,92,78,95,88]

grade.append(90)
grade.sort()
print("Sorted grades: ",grade)
print("Highest grade: ",grade[-1])
print("Lowest grade: ",grade[0])
print("Total number of grades: ",len(grade))

cart=["apple", "banana","milk","bread","eggs"]
apple_count= cart.count("apple")
print("Number of the apples: " ,apple_count)

milk_position=cart.index("milk")
print("Position of the milk:", milk_position)
cart.remove("apple")
print("Cart after removing apple:", cart)

#Pop an item
removed_item= cart.pop()
print("Is bana in the cart?: ", "banana" in cart) #**

print("Final cart: ", cart)
print()