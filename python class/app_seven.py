import tkinter as tk 
from math import *
pi = 22/7
root = tk.Tk() 
main_frame = tk.Frame(root)
main_frame.pack(anchor=tk.NW, expand=tk.YES, padx=10, pady=10, fill=tk.BOTH)
entry = tk.Entry(main_frame)
entry.bind('<Return>', lambda event: show_text(event, label))
entry.config(bg='#333333', fg='#eeeeee')
entry.config(font=('monospace', 30, 'bold'))
entry.pack(fill=tk.X, expand=tk.YES, side=tk.TOP)
def show_text(event=False,label=False):
    try:
        ans = eval(entry.get(),)
    except Exception:
        msg = "Invalid Input"
    else:
        msg = f"Result: {ans}"
    finally:
        label.config(text=msg)
        entry.delete(0, tk.END)
button = tk.Button(main_frame, text='Solve Eq', font=('monospace', 20, 'bold'))
button.config(width=8, )
button.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.YES)
def enter_button(event, enter=True):
    """ print(event.x)
    print(event.y)
    print(dir(event)) """
    if enter:
        button.config(fg='white', bg='#555555')
    else:
        button.config(fg='#333333', bg='white')
button.bind('<Enter>', lambda event:enter_button(event))
button.bind('<Leave>', lambda event:enter_button(event, False))
exit_button = tk.Button(main_frame, text="Exit", font=('monospace', 20, 'bold'))
exit_button.config(width=8, command=lambda : root.destroy())
exit_button.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.YES)
sub_frame = tk.Frame(root)
sub_frame.pack(fill=tk.BOTH, expand=tk.YES)
label = tk.Label(sub_frame, font=('Times', 25, 'bold'))
label.config(bg='#123456', fg='white', height=2)
button.config(command=lambda label=label:show_text(label=label))
label.pack(fill=tk.BOTH, expand=tk.YES)
#root.geometry('400x400')
root.mainloop()