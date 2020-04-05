def main():
    import tkinter as tk
    import json
    import random
    with open("menu.json", 'r') as f:
        data = json.load(f)
    main = tk.Tk()
    main.rowconfigure([0,1,2], minsize=50, weight=1)
    main.columnconfigure([0], minsize=50, weight=1)
    main.title("Main")
    meat = tk.Label(text=("Meat dish today", random.choice(list(data["meat"]))))
    meat.grid(row=0, column=0)
    veg = tk.Label(text=("Vegetable dish today", random.choice(list(data["veg"]))))
    veg.grid(row=1, column=0)
    soup = tk.Label(text=("Soup dish today", random.choice(list(data["soup"]))))
    soup.grid(row=2, column=0)
    main.mainloop()
main()
