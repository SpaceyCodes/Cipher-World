import tkinter as tk
from tkinter import filedialog
from cipher import encrypt
from decipher import decrypt
file_path_final = {}
def findfile():
    file_path = filedialog.askopenfilename()
    file_path_final[0] = file_path
    label2['text'] = file_path
    print(file_path_final)
    

def encryption():
    print(file_path_final)
    if numcol.get().find(';') > 0:
        decrypt(file_path_final[0], numcol.get())
    else:
        encrypt(file_path_final[0], numcol.get())

height = 500
width = 400
root = tk.Tk()
root.title('')
canvas = tk.Canvas(root, height = height, width = width)
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth = 1, relheight = 1)

topframe = tk.Frame(frame)
topframe.place(relwidth = 1, relheight = 0.1)
namelabel = tk.Label(topframe, text='Cipher World', font=("Courier", 30))
namelabel.place(anchor = 'center', relx = 0.5, rely = 0.5)



fileframe = tk.Frame(frame)
fileframe.place(anchor = 'n', relx = 0.5, rely = 0.1)
label1 = tk.Label(fileframe, text='File Path:')
label1.pack()
label2 = tk.Label(fileframe, text = 'None')
label2.pack()


inputcolumn = tk.Frame(frame)
labelforkeycolumn = tk.Label(inputcolumn, text='Number of column/Key:')
labelforkeycolumn.pack()
inputcolumn.place(anchor = 'n', relx = 0.5, rely = 0.5)
numcol = tk.Entry(inputcolumn)
numcol.pack()

bottombutton = tk.Frame(frame)
bottombutton.place(anchor = 'center', relx = 0.5, rely = 0.9)
choosefilebutton = tk.Button(bottombutton, text='Choose file', bg = "gray", command = findfile)
choosefilebutton.pack()
encryptbutton = tk.Button(bottombutton, text='{}'.format('Encrypt/Decrypt'), bg = "gray", command = encryption)
encryptbutton.pack()

root.mainloop()



