import tkinter as tk
master = tk.Tk() 
main_frame = tk.Frame(master)
main_frame.pack(fill=tk.X)
name = tk.Label(main_frame,text="Name: ", font=("Times", 20, "bold"))
name.pack(anchor=tk.NW,side=tk.LEFT, padx=30, pady=30)
entry = tk.Entry(main_frame,  font=("Times", 20, "bold"))
entry.pack(anchor=tk.NW, side=tk.LEFT, pady=30,)
show = tk.Button(master, text="SHOW", 
command=lambda: (print(entry.get()), entry.delete(0, tk.END)))
show.config(font=20, width=15, bg='#123456', fg='white')
show.pack(anchor=tk.NW, padx=40, side=tk.LEFT)
exit = tk.Button(master, text="EXIT",  command=lambda : master.quit())
exit.config(font=20, width=15, bg='red', fg='white')
exit.pack(anchor=tk.NW, padx=40, side=tk.LEFT)
master.geometry('500x400')
master.mainloop()