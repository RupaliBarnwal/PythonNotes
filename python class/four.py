import tkinter as tk

root = tk.Tk()

main_frame = tk.Frame(root)
main_frame.config(bg='red')
main_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=20)

text_label = tk.Label(main_frame, text="Hello World")
text_label.config(bg='#333333', fg='#eeeeee', font=('Times', 25, 'bold'),
    relief=tk.RAISED)
text_label.pack(fill=tk.X, expand=tk.YES, padx=20)

root.config(bg='black')
root.geometry('400x400')
root.mainloop()