from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import glob

# Create a window
root = Tk()
root.title('Image Viewer')
root.iconbitmap('Icon.ico')
# root.attributes('-fullscreen', True)
# root.geometry("800x800")


def openfolder():
    global img_list
    folders_path = filedialog.askdirectory()
    os.chdir(folders_path)
    l = ["*.jpg", "*.jfif", "*.png"]
    my_img = []
    for i in l:
        my_img.extend(glob.glob(i))
    sorted(my_img)
    img_list = []
    for i in my_img:
        img_list.append(ImageTk.PhotoImage(Image.open(i)))

    my_label = Label(image=img_list[0])
    my_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


folder = Button(root, text="Open Folder", command=openfolder)
folder.grid(row=2, column=1)
os.chdir("C:\\Users\\debra\\Pictures")


# For image use PhotoImage for GUI application
l = ["*.jpg", "*.jfif", "*.png"]
my_img = []
for i in l:
    my_img.extend(glob.glob(i))

sorted(my_img)

img_list = []
for i in my_img:
    img_list.append(ImageTk.PhotoImage(Image.open(i)))

if len(img_list) != 0:
    my_label = Label(image=img_list[0])
    my_label.grid(row=0, column=1, columnspan=3, padx=10, pady=10)


# Define Forward Button
def forward(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=img_list[img_num])
    my_label.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
    # we redefine the forward button
    button_forward = Button(
        root, text=">>", command=lambda: forward(img_num+1))
    button_forward.grid(row=0, column=4)
    # we redefine the back button
    button_back = Button(root, text="<<", command=lambda: backward(img_num-1))
    button_back.grid(row=0, column=0)

    # disable forward button when reach the end
    if img_num == (len(img_list)-1):
        button_forward = Button(root, text=">>", state=DISABLED)
        button_forward.grid(row=0, column=4)


# backward function
def backward(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=img_list[img_num])
    my_label.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
    # we redefine the forward button
    button_forward = Button(
        root, text=">>", command=lambda: forward(img_num+1))
    button_forward.grid(row=0, column=4)
    # we redefine the back button
    button_back = Button(root, text="<<", command=lambda: backward(img_num-1))
    button_back.grid(row=0, column=0)

    # disable backward button when reach the end of first image
    if img_num == 0:
        button_back = Button(root, text="<<", state=DISABLED)
        button_back.grid(row=1, column=0)


# initial button
back_button = Button(root, text="<<", state=DISABLED)
exit_button = Button(root, text="Exit Program", command=root.quit)
if len(img_list) == 1:
    forward_button = Button(root, text=">>", state=DISABLED)
else:
    forward_button = Button(
        root, text=">>", command=lambda: forward(1), padx=10, pady=10)

back_button.grid(row=0, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=0, column=4)

root.mainloop()
