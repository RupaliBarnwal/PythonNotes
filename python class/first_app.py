"""
    This is a basic tkinter application
"""
import tkinter as tk
# python module to create desktop application
# wxpython, kivi, PyQt

master = tk.Tk()
# Tk() class is used to create master window


master.wm_minsize(400, 400)
master.wm_maxsize(400, 400)
#icon on master window so use ico
master.iconbitmap('images/master.ico')
master.title('MyFirstApplication')
# updating title of your master window
master.mainloop()
# it holds your master window unitll you quit
# or you destroy your master window
