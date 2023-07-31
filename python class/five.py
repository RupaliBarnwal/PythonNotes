import tkinter as tk
#from PIL import Image
from PIL.ImageTk import PhotoImage

# python -m pip install pillow
# python -m pip install opencv-python
import cv2

root = tk.Tk()

#im = Image.open('images/test1.jpg')
#im.thumbnail((300,300))
#im.save('images/test2.jpg')
main_frame = tk.Frame(root)
main_frame.config(bg='red')
main_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=20)

text_label = tk.Label(main_frame, text="Hello World")
text_label.config(bg='#333333', fg='#eeeeee', font=('Times', 25, 'bold'),
    relief=tk.RAISED)
text_label.pack(fill=tk.X, expand=tk.YES, padx=20)

ph = PhotoImage(file="images/test2.jpg")
photo_label = tk.Label(main_frame, image=ph)
photo_label.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=20)


button = tk.Button(root, text="Exit")
button.config(fg='#eeeeee', bg="#123456", font=('monospace', 15, 'bold'))
def func(name):
    #print("hello world", name)
    print("Bye Bye".center(60,'_'))
    root.quit()
button.config(command=lambda name='sachin yadav': func(name)  )
button.pack(fill=tk.X)
root.config(bg='black')
#root.geometry('400x400')


root.mainloop()