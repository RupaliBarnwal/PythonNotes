import tkinter as tk 
root = tk.Tk() 
label = tk.Label(root, text='Hello World', font=35)
label.pack(fill=tk.X)
def new_window():
    win = tk.Toplevel(root)
    win.grab_set()
    lab = tk.Label(win, text="I am Groot", font=('monospace', 25, 'bold'))
    lab.pack(fill=tk.BOTH)
    def quit():
        win.grab_release()
        win.destroy()
    button = tk.Button(win, text='Exit', command=lambda: quit())
    button.pack(fill=tk.X)

button = tk.Button(root, text="Top Window")
button.config(font=30, command=new_window)
button.pack(fill=tk.X)
button1 = tk.Button(root, text="Exit")
button1.config(font=30, command=root.quit)
button1.pack(fill=tk.X)
root.mainloop() 