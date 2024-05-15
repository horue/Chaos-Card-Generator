import customtkinter as ct
from CTkMenuBar import *
from toolbar import *

def bar1(fm):
    f0=ct.CTkFrame(fm, width=99, height=20)
    f0.grid(column=0, row=0, padx=0, pady=(0,30), sticky='ew', columnspan=5)

    global o1
    o1 = ct.CTkSegmentedButton(f0, values=["Save", "Open", "Export", ""],corner_radius=50,fg_color='#dbdbdb', selected_color='#dbdbdb',unselected_color='#dbdbdb', text_color='black',selected_hover_color='#c0c0c0',command=get_command)
    o1.set("")
    selected_value = o1.get()
    o1.delete(selected_value)
    o1.grid(row=2, column=0, pady=10, padx=10)

def initial(root):

    fm=ct.CTkFrame(root)
    fm.pack(fill='both', expand=True, side='top')

    bar1(fm)

    f1=ct.CTkScrollableFrame(fm, width=400, height=300)
    f1.grid(column=0, row=1, padx=30)
    
    f2=ct.CTkScrollableFrame(fm, width=400, height=300)
    f2.grid(column=0, row=2, padx=30, pady=30)

    f3=ct.CTkFrame(fm, width=500, height=700)
    f3.grid(column=5, row=1)
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
    root.columnconfigure((0, 1, 2), weight=0)


    
    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main_screen()