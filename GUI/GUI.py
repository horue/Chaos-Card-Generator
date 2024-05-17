import customtkinter as ct
from CTkMenuBar import *
from  CustomTkinterMessagebox  import  *
from customtkinter import filedialog
from CTkSpinbox import *

elements = ['Fire', 'Water', 'Grass', 'Rock', 'Wind', 'Light', 'Dark']




def get_command(value):
    print("segmented button clicked:", value)
    if value == 'Save':
        CTkMessagebox.messagebox(title='Warning test', text='Save')
    if value == 'Open':
        filedialog.askopenfilename()
    if value == 'Export':
        CTkMessagebox.messagebox(title='Warning', text='Card exported.')

    o1.set("")

def bar1(fm):
    #f0=ct.CTkFrame(fm, width=99, height=20)
    #f0.grid(row=0, padx=0, pady=(0,30), sticky='ew', columnspan=True)

    global o1
    o1 = ct.CTkSegmentedButton(fm, values=["Save", "Open", "Export", ""],corner_radius=50,fg_color='#dbdbdb', selected_color='#dbdbdb',unselected_color='#dbdbdb', text_color='black',selected_hover_color='#c0c0c0',command=get_command)
    o1.set("")
    selected_value = o1.get()
    o1.delete(selected_value)
    o1.grid(row=2, column=0, pady=10, padx=10)

def frame1(f1):
    o1 = ct.CTkOptionMenu(f1, values=['Creature', 'Witchcraft'])
    o1.pack()

    l1a = ct.CTkLabel(f1, text="Card Name")
    l1a.pack()

    e1 = ct.CTkEntry(f1, width=200, border_color='Gray')
    e1.pack(padx=10)

    l2a = ct.CTkLabel(f1, text="Card Info")
    l2a.pack()

    e2 = ct.CTkEntry(f1, width=200, border_color='Gray')
    e2.pack(padx=10)

    l3a = ct.CTkLabel(f1, text='Card Effect')
    l3a.pack()

    e3 = ct.CTkTextbox(f1, height=200, width=700, border_color='Gray', border_width=2)
    e3.pack(padx=100)

    l4 = ct.CTkLabel(f1, text='Card Element')
    l4.pack()

    o2 = ct.CTkOptionMenu(f1, values=elements)
    o2.pack()

    l4a = ct.CTkLabel(f1, text='Mana Cost')
    l4a.pack()

    s1 = ct.IntVar()
    s1 = CTkSpinbox(f1,
          start_value = 1,
          min_value = 1,
          max_value = 11,
          scroll_value = 2,
          variable = s1)
    s1.pack()

    l5a = ct.CTkLabel(f1, text='Card Power')
    l5a.pack()

    s2 = ct.IntVar()
    s2 = CTkSpinbox(f1,
          start_value = 1,
          min_value = 1,
          max_value = 16,
          scroll_value = 2,
          variable = s2)
    s2.pack()


    l6a = ct.CTkLabel(f1, text='Card ID/Date')
    l6a.pack()

    e4 = ct.CTkTextbox(f1, height=50, width=700, border_color='Gray', border_width=2)
    e4.pack(padx=100)



def initial(root):
    fh=ct.CTkFrame(root)
    fh.pack(fill='x', anchor='n')

    fm=ct.CTkFrame(root, height=20, fg_color='#ffffff')
    fm.pack(fill='both', expand=True, anchor='s')
    
    bar1(fh)

    f1=ct.CTkScrollableFrame(fm, width=400, height=620, label_text='Card Configuration')
    f1.grid(column=0, row=1, padx=30, pady=(30,0))

    frame1(f1)


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