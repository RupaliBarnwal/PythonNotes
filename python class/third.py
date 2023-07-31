import tkinter as tk

root = tk.Tk()
# Tk() is used to create root window


hello_label = tk.Label(root, text="Hello World")

hello_label.config(font=("Monospace", 30, 'italic', 'bold'),
            fg='red', bg='#cccccc')

bye_label = tk.Label(root, text="Bye World")
bye_label.config(font=("Times", 20, 'bold'),
            fg='blue', bg='#cccccc')
bye_label.pack(fill=tk.X, pady=20, ipady=30)

hello_label.pack(fill=tk.X, ipady=30, ipadx=20 ) #ipadx=0, side=tk.LEFT, fill=tk.BOTH, expand=tk.YES, ) # anchor=tk.N
#jpeg, png are not allowed as icon image you have to use .ico files(bitmap)
#root.iconbitmap('fname')
ph = tk.PhotoImage(file='images/master.png')
root.iconphoto(False, ph)
root.title("My First Application Ever")
root.geometry('400x400')

# title of our master window
root.mainloop()
# to hold our application untill we close it