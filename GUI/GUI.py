import customtkinter as ct

def initial(root):
    l1 = ct.CTkLabel(root, text='Chaos Card Generator - Main Screen')
    l1.pack()
    print(1)


def main_screen():
    root = ct.CTk()
    root.geometry("400x500")
    root.title("Chaos Card Generator")

    
    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main_screen()