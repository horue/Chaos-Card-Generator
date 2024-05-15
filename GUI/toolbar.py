import customtkinter as ct

def get_command(value):
    print("segmented button clicked:", value)
    o1.set("")


def bar(root):
    f0=ct.CTkFrame(root, width=10, height=20)
    f0.grid(column=0, row=0, padx=0, pady=(0,30), sticky='ew', columnspan=5)

    global o1
    o1 = ct.CTkSegmentedButton(f0, values=["Save", "Open", "Export", ""],corner_radius=50,fg_color='#dbdbdb', selected_color='#dbdbdb',unselected_color='#dbdbdb', text_color='black',selected_hover_color='#c0c0c0',command=get_command)
    o1.set("")
    selected_value = o1.get()
    o1.delete(selected_value)
    o1.grid(row=2, column=0, pady=10, padx=10)
