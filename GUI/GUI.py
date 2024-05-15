import customtkinter as ct

def initial(root):
    
    l1 = ct.CTkLabel(root, text='Chaos Card Generator - Main Screen')
    l1.grid(column=3, row=1)

    f0=ct.CTkFrame(root, width=10, height=20)
    f0.grid(column=0, row=0, padx=0, pady=(0,30), sticky='ew', columnspan=5)

    f1=ct.CTkScrollableFrame(root, width=400, height=300)
    f1.grid(column=0, row=1, padx=10)
    
    f2=ct.CTkScrollableFrame(root, width=400, height=300)
    f2.grid(column=0, row=2, padx=30, pady=30)

    l1a = ct.CTkLabel(f1, text="Card Name")
    l1a.pack()

    e1 = ct.CTkEntry(f1, width=200, border_color='Gray')
    e1.pack(padx=10)

    l2a = ct.CTkLabel(f1, text='Card Effect')
    l2a.pack()

    e2 = ct.CTkTextbox(f1, height=200, width=200, border_color='Gray', border_width=2)
    e2.pack(padx=100)


    print(1)


def main_screen():
    root = ct.CTk()
    root.geometry("400x500")
    root.title("Chaos Card Generator")
    root.rowconfigure(index=3)
    root.columnconfigure((0, 1, 2, 3, 4), weight=1)


    
    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main_screen()