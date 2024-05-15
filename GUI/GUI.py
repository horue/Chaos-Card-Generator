import customtkinter as ct

def p():
    print(1)

def initial(root):

    f0=ct.CTkFrame(root, width=10, height=20)
    f0.grid(column=0, row=0, padx=0, pady=(0,30), sticky='ew', columnspan=5)

    o1 = ct.CTkOptionMenu(f0, default_text='File',values=['Export', "Save", "Open"], command=lambda:print(1))
    o1.grid(row=0, column=0, pady=10, padx=10)


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