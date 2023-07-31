import tkinter as tk 

root = tk.Tk()

v = tk.StringVar()
v.set("PYTHON")
choice = tk.Label(root, text="""Choose a 
Programming Language""", font=('Times', 30, 'bold'),
fg='red', justify=tk.LEFT, padx=20, pady=20)

choice.pack(fill=tk.X, expand=tk.YES)

b1 = tk.Radiobutton(root, text="Python",
            padx=20, variable=v, value='PYTHON',
            font=("Monospace", 20, "bold" ),
            )
b1.pack(anchor=tk.W)

b2 = tk.Radiobutton(root, text="Java",
            padx=20, variable=v, value="JAVA",
            font=("Monospace", 20, "bold" ),
            )
b2.pack(anchor=tk.W)

show = tk.Label(root, text="", bg='red', fg='white',
    font=('Times', 30, 'bold'), justify=tk.LEFT, padx=20)
show.pack(fill=tk.X, expand=tk.YES) 

submit = tk.Button(root, text='submit', bg='black', fg='white', height=2,
        font=("Monospace", 20, "bold"),padx=20,command=lambda : show_text() )
submit.pack(fill=tk.X, expand=tk.YES)
def show_text():
    show.config(text=f'your Selection is {v.get()}')

root.mainloop()