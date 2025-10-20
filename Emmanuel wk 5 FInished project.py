'''

Software Development
Emmanuel Chinonso Francis aims to be a junior python developer by the end of this year,

Additional Creativity: I added a message that will be the users feedback based in the
classes of food on their list and also tell them why the item on their list is great.

Please follow to the end that is answer the prompts till the user in other to get the possible class of food
'''

try:

    major_food = {
        "Carbohydrate": ["Hamburger", "Bread", "Cheese", "Rice", "Corn", "Pasta", "Yam"],
        "Protein": ["chicken", "Steak", "Peanut butter,", "Fish", "Beef", "Beans"],
        "Vitamins": ["Juice", "Eggs", "Kale salad", "Apples", "Orange", "Strawberry"],
        "Fats & Oil":  ["French fries", "Cheeseburgers", "Butter"],
        "Minerals": ["Milk", "Spinach", "Bananas" ],
        "Water": ["Bottled water", "Soup", "Water", "Coconut water"],
        "Fiber": ["Grain", "Oatmeal", "Black beans", "vegetables"]
    }

    print("Please enter the items of the shopping list (type: quit to fini"
          ""
          ""
          ""
          ""
          ""
          ""
          ""
          "sh): ")
    the_list = []
    item = None

    while item != "Quit":
        item = input("Item: ").title()

        if item != "Quit":
            the_list.append(item)
    print("")
    print("The shopping list is:")

    for items in the_list:
        print(f"{items}")

    print("")
    print("The shopping list with indexes is:")

    for i in range(len(the_list)):
        items = the_list[i]
        print(f"{i}. {items}")

    print("")
    change_item = int(input("Enter the index(number) of the item you like to change: "))
    replaced_item = input("What is the new item: ").title()
    if replaced_item != "":
        the_list.pop(change_item)
        the_list.insert(change_item, replaced_item)

    print("")
    print("The shopping list with indexes is:")

    for i in range(len(the_list)):
        items = the_list[i]
        print(f"{i}. {items}")

    for category, foods in major_food.items():
        for food in foods:
            for items in the_list:
                if food in items:
                    print(f"I love this list! It contains {food}, which is great for {category}.")
                else:
                  pass
except ValueError:
    print("Please read instructions well  nd enter a valid input next time.")