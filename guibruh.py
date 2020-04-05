import tkinter as tk
import json
import os


def main():

    with open("menu.json", 'r') as f:
        data = json.load(f)

    menu_dict = {"meat":data["meat"],
             "veg":data["veg"],
             "soup":data["soup"]
    }
    def meat():
        menu_dict["meat"].append(entry.get())
        with open("menu.json", "w") as json_file:
            json.dump(menu_dict, json_file)
        labelthree["text"] = str(menu_dict)
    def veg():
        menu_dict["veg"].append(entry.get())
        with open("menu.json", "w") as json_file:
            json.dump(menu_dict, json_file)
        labelthree["text"] = str(menu_dict)
        
    def soup():
        menu_dict["soup"].append(entry.get())
        with open("menu.json", "w") as json_file:
            json.dump(menu_dict, json_file)
        labelthree["text"] = str(menu_dict)
    def clear():
        menu_dict["meat"] = []
        menu_dict["veg"] = []
        menu_dict["soup"] = []
        with open("menu.json", "w") as json_file:
            json.dump(menu_dict, json_file)
        labelthree["text"] = str(menu_dict)
    def end():
        bruh.destroy()
        import guimain
        
    bruh = tk.Tk()
    bruh.rowconfigure([0,1,2,3,4], minsize=50, weight=1)
    bruh.columnconfigure([0, 1,2], minsize=50, weight=1)
    bruh.title("Bruh")
   
    labeltwo = tk.Label(text="Which dish do you want to add?")
    labeltwo.grid(row=0, column=1)
    entry = tk.Entry()
    entry.grid(row=1, column=1)
    labelthree = tk.Label(text = str(menu_dict))
    labelthree.grid(row=4, column=1)
    
    meat = tk.Button(master=bruh, text="Meat", command=meat)
    meat.grid(row=2, column=0, sticky="nsew")
    veg = tk.Button(master=bruh, text="Vegetable", command=veg)
    veg.grid(row=2, column=1, sticky="nsew")
    soup = tk.Button(master=bruh, text="Soup", command=soup)
    soup.grid(row=2, column=2, sticky="nsew")
    end = tk.Button(master=bruh, text="End", command=end)
    end.grid(row=3, column=1, sticky="nsew")
    end = tk.Button(master=bruh, text="Clear", command=clear)
    end.grid(row=3, column=0, sticky="nsew")
    bruh.mainloop()
main()
