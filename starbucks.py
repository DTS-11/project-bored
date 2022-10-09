import time


menu = ["coffee", "tea", "cappuccino", "latte", "mocha", "ice-cream"]
price = {
    "coffee": 5,
    "tea": 5,
    "cappuccino": 8,
    "latte": 10,
    "mocha": 10,
    "ice-cream": 3, 
}
user_selected_items = []
select_another_item = f"\nPlease select another item from the menu:\n{', '.join(menu)}\n\n"
other_items_question = "\nAnything else you want? (y/n): "
goodbye = "\nThank you for your purchase, have a great day!"


print("\n========================")
print("WELCOME TO STARBUCKS!!!")
print("========================\n")

name = input("What is your name? ")
print(f"Welcome {name}, to the DTS version of Starbucks!")

res = input(f"\nPlease select an item from the menu:\n{', '.join(menu)}\n\n")

if res not in menu:
    print("Sorry, that item is not in the list.")

else:
    if res == "coffee".lower():
        user_selected_items.append("coffee")
        res2 = input(other_items_question)

        if res2 == 'y':
            choice = input(select_another_item)
            if choice in menu:
                user_selected_items.append(choice)
                print(f"Total: ${price['coffee'] + price[choice]}")
                time.sleep(1.25)
                print(goodbye)
        elif res2 == 'n'.lower():
            print(goodbye)

    if res == "tea".lower():
        user_selected_items.append("tea")
        res2 = input(other_items_question)

        if res2 == 'y':
            choice = input(select_another_item)
            if choice in menu:
                user_selected_items.append(choice)
                print(f"Total: ${price['tea'] + price[choice]}")
                time.sleep(1.25)
                print(goodbye)
        elif res2 == 'n'.lower():
            print(goodbye)

    if res == "cappuccino".lower():
        user_selected_items.append("cappuccino")
        res2 = input(other_items_question)

        if res2 == 'y':
            choice = input(select_another_item)
            if choice in menu:
                user_selected_items.append(choice)
                print(f"Total: ${price['cappuccino'] + price[choice]}")
                time.sleep(1.25)
                print(goodbye)
        elif res2 == 'n'.lower():
            print(goodbye)

    if res == "latte".lower():
        user_selected_items.append("latte")
        res2 = input(other_items_question)

        if res2 == 'y':
            choice = input(select_another_item)
            if choice in menu:
                user_selected_items.append(choice)
                print(f"Total: ${price['latte'] + price[choice]}")
                time.sleep(1.25)
                print(goodbye)
        elif res2 == 'n'.lower():
            print(goodbye)

    if res == "mocha".lower():
        user_selected_items.append("mocha")
        res2 = input(other_items_question)

        if res2 == 'y':
            choice = input(select_another_item)
            if choice in menu:
                user_selected_items.append(choice)
                print(f"Total: ${price['mocha'] + price[choice]}")
                time.sleep(1.25)
                print(goodbye)
        elif res2 == 'n'.lower():
            print(goodbye)

    if res == "ice-cream".lower():
        user_selected_items.append("ice-cream")
        res2 = input(other_items_question)

        if res2 == 'y':
            choice = input(select_another_item)
            if choice in menu:
                user_selected_items.append(choice)
                print(f"Total: ${price['ice-cream'] + price[choice]}")
                time.sleep(1.25)
                print(goodbye)
        elif res2 == 'n'.lower():
            print(goodbye)