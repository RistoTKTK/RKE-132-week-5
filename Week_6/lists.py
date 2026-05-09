import random

""" item1 = "apples"
item2 = "bread"
item3 = "milk"
item4 = "eggs" """

""" shopping_list = ["cheese","apples", "bread", "cheese", "milk", "eggs", "cheese"] """

# len()
""" print(f"We have {len(shopping_list)} items on the list.") """

#append()
""" shopping_list.append("yougurt") """

#extend()
""" shopping_list.extend(["flour", "sugar", "baking powder"]) """ 

#remove()
""" shopping_list.remove("cheese") """

""" for item in shopping_list.copy():
    if item == "cheese":
        shopping_list.remove(item) """

#count()
""" n = shopping_list.count("cheese")
print(f"there are {n} cheese items on the list.") """

# index()
""" apple_index = shopping_list.index("apples")
shopping_list[apple_index] = "bananas" """
""" print(f"you can find apples at {apple_index}") """

""" shopping_list = ["cheese","apples", "bread", "cheese", "milk", "eggs", "cheese"] """

# item in shopping_list

""" found = "milk" in shopping_list """
""" found = False """
""" for item in shopping_list:
    if item == "soy milk": 
        found = True
        break """

""" if found:
    print("Milk is allready on the list.")
else:
    print("there is no milk on the list") """

#sort()


""" shopping_list = ["cheese","apples", "bread", "cheese", "milk", "eggs", "cheese"] """
""" 
print(f"We have {len(shopping_list)} items on the list.") """

""" print(shopping_list)

shopping_list.sort(reverse=True)

print(shopping_list) """

""" for item in shopping_list:
    print(item) """

#reverse()
""" shopping_list = ["cheese","apples", "bread", "cheese", "milk", "eggs", "cheese"] """

""" print(shopping_list)
shopping_list.reverse()
print(shopping_list) """

shopping_list = ["cheese","apples", "bread", "cheese", "milk", "eggs", "cheese"]

#random
random_item = random.choice(shopping_list)
print(random_item)

""" for item in shopping_list:
    print(item) """