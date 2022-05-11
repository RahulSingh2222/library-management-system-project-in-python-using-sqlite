import os
import tkinter as tk

root=tk.Tk()

canvas1=tk.label(root,text='upgrade PIP',bg='lightsteelblue2')
label1.config(front=('helvetica',20))
canvas1.create_window(150,80,window=lable1)

def upgradePIP ():
    os.system('start amd /k python.exe -m pip install --upgrade pip')

button1=tk.Button(text='   Upgrade PIP     ',command=upgradePIP,bg='green',fg='white',font=('helvetica',12, 'bold'))
canvas1.create_window(150,180,window=button1)

root.mainloop()
