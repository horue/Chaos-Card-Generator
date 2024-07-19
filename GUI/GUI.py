import customtkinter as ct
from CTkMenuBar import *
from  CustomTkinterMessagebox  import  *
from customtkinter import filedialog
from CTkSpinbox import *
from cardgenerator_u import *
from romanconverter import *
from cardsaver import *
import PIL

config = open('GUI\elements.ini', 'r')
config_read = config.read()
elements = config_read.split(',')
output_temp = r'C:\Users\jorge\Projetos\Chaos-Card-Generator\temp.png'


def create_temp():
    change_name(new_name=str(name.get()))
    change_type(new_type=str(e2.get()))
    change_mana(new_mana=write_roman(s1.get()))
    change_power(new_power=str(s2.get()))
    change_frame(new_frame=str(o3.get()))
    change_class(new_class=str(o7.get()))
    change_info(new_info=e4.get('1.0', 'end-1c').replace('\n', '\r'))
    change_effect(new_effect=e3.get('1.0', 'end-1c').replace('\n', '\r'))
    new_image = Image.open(output_temp)
    show_image(new_image)

def create_final():
    change_name(new_name=str(name.get()))
    change_effect(new_effect=e3.get('1.0', 'end-1c').replace('\n', '\r'))
    CTkMessagebox.messagebox(title='Warning', text='Card exported.')
    save_final(name=str(name.get()))

def get_command(value):
    print("segmented button clicked:", value)
    if value == 'Save':
        save_json(file=name.get(), nome=name.get(), eff=e3.get('1.0', 'end-1c'))
        CTkMessagebox.messagebox(title='Warning test', text='Save')
    if value == 'Open':
        filedialog.askopenfilename()
    if value == 'Generate':
        create_temp()
    if value == 'Export':
        create_final()
    o1.set("")

def show_image(new_image):
    ph = ct.CTkImage(light_image=new_image, dark_image=new_image, size=(744/2, 1039/2))
    i1.configure(image=ph)


def bar1(fm):
    #f0=ct.CTkFrame(fm, width=99, height=20)
    #f0.grid(row=0, padx=0, pady=(0,30), sticky='ew', columnspan=True)

    global o1
    o1 = ct.CTkSegmentedButton(fm, values=["", "Save", "Open", "Generate",'Export'],corner_radius=50,fg_color='#dbdbdb', selected_color='#dbdbdb',unselected_color='#dbdbdb', text_color='black',selected_hover_color='#c0c0c0',command=get_command)
    o1.set("")
    selected_value = o1.get()
    o1.delete(selected_value)
    o1.grid(row=2, column=0, pady=10, padx=10)

def frame1(f1):
    global o7
    o7 = ct.CTkOptionMenu(f1, values=['Creature', 'Witchcraft'])
    o7.pack()

    l1a = ct.CTkLabel(f1, text="Card Name")
    l1a.pack()

    global name
    name = ct.CTkEntry(f1, width=200, border_color='Gray')
    name.pack(padx=10)

    l2a = ct.CTkLabel(f1, text="Card Info")
    l2a.pack()

    global e2
    e2 = ct.CTkEntry(f1, width=200, border_color='Gray')
    e2.pack(padx=10)

    l3a = ct.CTkLabel(f1, text='Card Effect')
    l3a.pack()

    global e3
    e3 = ct.CTkTextbox(f1, height=200, width=700, border_color='Gray', border_width=2)
    e3.pack(padx=100)

    l4 = ct.CTkLabel(f1, text='Card Element')
    l4.pack()

    global o2
    o2 = ct.CTkOptionMenu(f1, values=elements)
    o2.pack()

    l4a = ct.CTkLabel(f1, text='Mana Cost')
    l4a.pack()


    global s1
    s1 = ct.IntVar()
    s1 = CTkSpinbox(f1,
          start_value = 1,
          min_value = 1,
          max_value = 11,
          scroll_value = 1,
          variable = s1)
    s1.pack()

    l5a = ct.CTkLabel(f1, text='Card Power')
    l5a.pack()


    global s2
    s2 = ct.IntVar()
    s2 = CTkSpinbox(f1,
          start_value = 1,
          min_value = 0,
          max_value = 16,
          scroll_value = 1,
          variable = s2)
    s2.pack()


    l6a = ct.CTkLabel(f1, text='Card ID/Date')
    l6a.pack()


    global e4
    e4 = ct.CTkTextbox(f1, height=50, width=700, border_color='Gray', border_width=2)
    e4.pack(padx=100)

    l7a = ct.CTkLabel(f1, text='Card Frame')
    l7a.pack()

    global o3
    o3 = ct.CTkOptionMenu(f1, values=['Normal', 'Extended'])
    o3.pack()


def frame2(f2):
    global i1
    i1 = ct.CTkLabel(f2, text='')
    i1.pack(pady=15)





def initial(root):
    fh=ct.CTkFrame(root)
    fh.pack(fill='x', anchor='n')

    fm=ct.CTkFrame(root, height=20, fg_color='#ffffff')
    fm.pack(fill='both', expand=True, anchor='s')
    
    bar1(fh)

    f1=ct.CTkScrollableFrame(fm, width=400, height=620, label_text='Card Configuration')
    f1.grid(column=0, row=1, padx=30, pady=(30,0))

    frame1(f1)

    f2=ct.CTkScrollableFrame(fm, width=750, height=620, label_text='Card')
    f2.grid(column=1, row=1, padx=30, pady=(30,0))

    frame2(f2)


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