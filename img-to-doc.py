import os
import PIL.Image
from pytesseract import *
from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()  # creating tkinter window
root.geometry('500x200')  # setting window size
root.title('Image to Doc Converter')  # setting window title
root.wm_iconbitmap('icon.ico')  # setting window icon

# calling pytesseract from directory
pytesseract.tesseract_cmd = r'C:/Users/MadGeek/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

# browse file function
def browsefunc():
    global filename 
    filename = filedialog.askopenfilename(title='Select a file', filetypes=(('JPEG (*.JPG; *.JPEG; *.JPE)', '*.jpg'), ('PNG (*.PNG)', '*.png'), ('All Files (*.*)', '*.*')))
    path.set(filename)

# open source directory function
def source_dir():
    try:
        os.startfile(os.path.split(filename)[0])
    except:
        messagebox.showinfo(title='Warning', message='No directory found!')

# open file function
def file_dir():
    try:
        fname = os.path.split(filename)[0] + '/' + os.path.splitext(os.path.basename(filename))[0] + '.doc'
        os.startfile(fname)
    except:
        messagebox.showinfo(title='Warning', message='No file found!')

# image to text conversion function
def imgtotext():
    try: 
        img = PIL.Image.open(filename)				
        result = pytesseract.image_to_string(img)
        file_name = os.path.splitext(os.path.basename(filename))[0] + '.doc'
        text_file = open(os.path.join((os.path.split(filename)[0] + '/'), file_name), "w") 
        text_file.write(result)
        text_file.close()
        root.geometry('500x250')
        l2 = Label(root, text='File has been saved.', font='roboto').place(relx=0.5, rely=0.9, anchor=CENTER)  
    except:
        messagebox.showinfo(title='Warning', message='Please choose a correct file!')

# label
l1 = Label(root, text='Image to Doc Converter', font=('roboto bold', 20)).place(relx=0.5, rely=0.2, anchor=CENTER)
# variable
path = StringVar()
# entry
e1 = Entry(root, width=50, textvariable=path).place(relx=0.4, rely=0.5, anchor=CENTER)
# buttons
b1 = Button(root, text='Browse a file', font=('roboto', 10), command=browsefunc).place(relx=0.85, rely=0.5, anchor=CENTER)
b2 = Button(root, text='Convert', font=('roboto bold', 10), bg='green', fg='white', command=imgtotext).place(relx=0.3, rely=0.75, anchor=CENTER)
b3 = Button(root, text='Source Folder', font=('roboto bold', 10), bg='gray', fg='white', command=source_dir).place(relx=0.5, rely=0.75, anchor=CENTER)
b4 = Button(root, text='Open File', font=('roboto bold', 10), bg='gray', fg='white', command=file_dir).place(relx=0.7, rely=0.75, anchor=CENTER)

root.mainloop()