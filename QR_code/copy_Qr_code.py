import qrcode
from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('QR Code Generator')
ws.geometry('600x400')
ws.config(bg='#6a9a8d')



def generate():
    img = qrcode.make(msg.get())
    type(img)
    img.save(f'{save_name.get()}.png')
    Label(ws, text='File Saved!', fg='green').pack()


frame = Frame(ws, bg='#6a9a8d',height=30,width=30)
frame.pack(expand=True)

Label(
    frame,
    text='URL',
    font=('Times', 24),
    bg='#6a9a8d',
).grid(row=0, column=0, sticky='s')

msg = Entry(frame)
msg.grid(row=0, column=1)

Label(
    frame,
    text='Save as',
    font=('Times', 24),
    bg='#6a9a8d',
).grid(row=1, column=0, sticky='w')

save_name = Entry(frame)
save_name.grid(row=1, column=1)

btn = Button(
    ws,
    text='Generate QR code',
    
    command=generate
)
btn.pack()

ws.mainloop()
