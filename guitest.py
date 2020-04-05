import tkinter as tk
def main():
    def bruh():
        window.destroy()
        import guibruh
        
    def m():
        window.destroy()
        import guimain
    window = tk.Tk()
    window.rowconfigure([0,1], minsize=50, weight=1)
    window.columnconfigure([0, 1], minsize=50, weight=1)
    window.title("Menu")

    label = tk.Label(text="Do you want to go to the randomisation or the menu?")
    label.grid(row=0, column=0)
    
    bruhbutt = tk.Button(master=window, text="Menu", command=bruh)
    bruhbutt.grid(row=1, column=0, sticky="nsew")

    menubutt = tk.Button(master=window, text="Randomisation", command=m)
    menubutt.grid(row=1, column=1, sticky="nsew")

    window.mainloop()
main()


