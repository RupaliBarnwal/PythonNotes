from tkinter import *

lang_list = [ 'Java', 'C', 'C++', 'Python', 'Ruby']

master = Tk()

svar = [ IntVar() for _ in range(len(lang_list)) ] 

Label(master, text="Choose Language", font=('monospace', 30, 'bold'),
    pady=30, padx=30, justify=LEFT).pack(side=TOP, fill=X, expand=YES)

   
Button(master, text='Show', command=lambda : show(), relief=GROOVE,bg='gray',
 font=('monospace', 30, 'bold') ).pack(fill=X, side=BOTTOM, )

for i,choice in enumerate(lang_list):
    Checkbutton(master, text=choice, variable=svar[i], 
    font=('monospace', 30, 'bold')).pack(fill=X, expand=YES, side=LEFT)
 

def show():
    for lang in lang_list:
        print(f"{lang:>10}", end=', ')
    print()
    for var in svar:
        print(f"{var.get():>10}", end=', ')
        var.set(0)
    print()
master.mainloop()
