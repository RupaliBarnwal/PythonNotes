import tkinter as tk 


root = tk.Tk() 

e1 = tk.Entry(root, font=35)
e1.pack(fill=tk.X)

b = tk.Button(root, text="OPEN")
b.config(text="OPEN FILE", font=35, command=lambda :open_file())
b.pack(fill=tk.X)
button = tk.Button(root, text="EXIT", bg='#cccccc', fg='red', font=35)
button.config(command=lambda :root.quit())
button.pack(fill=tk.BOTH, )


def open_file():
    path = e1.get()
    with open(path) as fp:
        data = fp.read()
        fp.close()
    win = tk.Toplevel(root)
    win.grab_set()
    label = tk.Message(win, text=data)
    label.config(bg='cyan', fg='black', font=('Times', 20, 'italic'))
    label.pack(fill=tk.BOTH)
    def exit_me():
        win.grab_release()
        win.quit()
    button = tk.Button(win, text="EXIT", bg='#cccccc', fg='red', font=35)
    button.config( command=lambda :exit_me())
    button.pack(fill=tk.BOTH,)

root.mainloop()