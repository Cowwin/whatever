import json
import os
with open("/Users/truemac/Desktop/menu/menu.json", 'r') as f:
        data = json.load(f)
menu_dict = {"meat":data["meat"],
             "veg":data["veg"],
             "soup":data["soup"]
}
item = ""
remove = input("Do you want to clear file? Y/N")
if(remove == "Y" or remove == "y"):
    menu_dict = {"meat":[],
             "veg":[],
             "soup":[]
    }

while True:
    
    item = input("What do you want to add to the menu? Meat, vegetable, or soup?")
    if(item == "meat" or item == "Meat"):
        while True:
            menu_dict["meat"].append(input("Which meat dish would you like to add to the menu?"))
            print("Your current menu:",menu_dict)
            x = input("Would you like to add another meat dish? Y/N")
            if (x == "N" or x == "n"):
                print ('current choice is', x)
                break
    elif(item == "vegetable" or item == "Vegetable"):
        while True:
            menu_dict["veg"].append(input("Which vegetable dish would you like to add to the menu?"))
            print("You current menu:", menu_dict)
            x = input("Would you like to add another vegetable dish? Y/N")
            if (x == "N" or x == "n"):
                print ('current choice is', x)
                break
    elif(item == "soup" or item == "Soup"):
        while True:
            menu_dict["soup"].append(input("Which soup dish would you like to add to the menu?"))
            print("You current menu:", menu_dict)
            x = input("Would you like to add another soup dish? Y/N")
            if (x == "N" or x == "n"):
                print ('current choice is', x)
                break
    else:
        print("Please enter meat/vegetable/soup")
    y = input("Do you want to quit? Y/N")
    if(y == "Y" or y == "y"):
        break

    
with open("menu.json", "w") as json_file:
    json.dump(menu_dict, json_file)
import main
    
