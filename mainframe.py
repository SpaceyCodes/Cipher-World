import tkinter as tk
from tkinter import filedialog


def findfile():
    file_path = filedialog.askopenfilename()
    label = tk.Label(fileframe, text=file_path)
    label.pack()
    root.clipboard_clear()
    root.clipboard_append(file_path)
    root.update()
    return file_path

height = 500
width = 400
root = tk.Tk()
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
label = tk.Label(fileframe, text='File Path:')
label.pack()

button = tk.Button(frame, text='Test Button', bg = "gray", command = findfile)
button.place(anchor = 'center', relx = 0.5, rely = 0.9)


root.mainloop()



'''
root.withdraw()

file_path = filedialog.askopenfilename()

print(file_path)
'''
