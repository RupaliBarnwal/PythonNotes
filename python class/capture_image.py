# python -m pip install Opencv-python
import tkinter as tk
import PIL
from PIL.ImageTk import PhotoImage
import cv2
width,height=640, 480
root = tk.Tk()
# fourcc - video enconding

device = cv2.VideoCapture(0)
device.set(cv2.CAP_PROP_FRAME_WIDTH, width)
device.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # X V I D
out_strem = cv2.VideoWriter('DCMI/myvideo.avi', fourcc, 30, (width, height))
var = 1

def exit_func():
    device.release()
    out_strem.release()
    root.destroy()
def click_image():
    global var 
    flag, image = device.read()
    image = cv2.flip(image, 1)
    path = f'DCMI/image_{var}.jpg'
    var += 1
    cv2.imwrite(path, image)
    print("Image Saved : ", path.split('/')[-1])

def show_video(save=False):
    flag, image = device.read()
    out_strem.write(image)
    image = cv2.flip(image, 1)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = PIL.Image.fromarray(img)
    imgtk = PhotoImage(image=image)
    label.config(image=imgtk)
    label.imgtk=imgtk
    label.after(1, lambda :show_video())
    


label = tk.Label(root,)
label.pack(anchor=tk.NW, fill=tk.BOTH, expand=tk.YES)
label.after(1, lambda :show_video())

click = tk.Button(root, text="Click", 
            command=lambda :click_image(), font=('Courier', 20, 'bold'),
fg='red', bg='#cccccc')
click.pack( fill=tk.X, expand=tk.YES)

exit_button = tk.Button(root, text='Exit', 
        command=lambda : exit_func(),
         font=('Courier', 20, 'bold'),
    bg='red', fg='#cccccc')
exit_button.pack(fill=tk.X, expand=tk.YES)
root.mainloop()


# canvas
# scroll bar 
# list
# menubar
# filedialog box
# sliders 