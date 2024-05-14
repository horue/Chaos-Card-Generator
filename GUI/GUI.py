import customtkinter as ct

def initial(root):
    l1 = ct.CTkLabel(root, text='Chaos Card Generator - Main Screen')
    l1.pack()

    e1 = ct.CTkEntry(root, placeholder_text='Card Name', width=200, border_color='Gray')
    e1.pack(padx=10, pady=20)

    e2 = ct.CTkTextbox(root, height=200, width=200, border_color='Gray', border_width=2)
    e2.pack(padx=100)


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