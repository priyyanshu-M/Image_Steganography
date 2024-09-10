import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from stegano import lsb

def open_encode(stegno):
    stegno.title('STEGNOGRAPHY APP')
    stegno.geometry("900x500")
    image_path = "D:/virtual studio code/PYTHON/STEGANOGRAPHY/stegano1.png"
    image = Image.open(image_path)
    photo_image = ImageTk.PhotoImage(image)

    bg_image = tk.Label(stegno, image=photo_image)
    bg_image.photo = photo_image  
    bg_image.place(relheight=1, relwidth=1)

    text_label = tk.Label(stegno, text='STEGANOGRAPHY(ENCODING MESSAGE)', font=('Georgia', 30),
                           fg="brown", background="cadetblue")
    text_label.pack()

    label1 = tk.Label(stegno, text="Secret Message :-", font=('Georgia', 12))
    label1.place(relx=0.1, rely=0.3)

    entry = tk.Entry()
    entry.place(relx=0.4, rely=0.3, relheight=0.1, relwidth=0.5)

    label2 = tk.Label(stegno, text="File Name :-",font=('Georgia', 10))
    label2.place(relx=0.1, rely=0.6)

    entrysave = tk.Entry()
    entrysave.place(relx=0.4, rely=0.6, relheight=0.08, relwidth=0.2)

    def openfile():
        global fileopen
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetype=(("jpeg file", "*.jpg"), ("all file", "*.*")))
        label3 = tk.Label(text=fileopen)
        label3.place(relx=0.6, rely=0.6)

    def encode():
        response = messagebox.askyesno("pop up", "Do you want to encode")
        if response:
            try:
                message = entry.get()
                image = lsb.hide(fileopen, message)
                image.save(entrysave.get() + '.png')
                messagebox.showinfo("pop up", "Successfully encoded")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("pop up", "Unsuccessful")

    buttonselect = tk.Button(stegno, text="Select File", font=('Georgia', 10),
                              bg="green", fg="white", width=15, height=3, command=openfile)
    buttonselect.place(relx=0.1, rely=0.4)

    buttonencode = tk.Button(stegno, text="Encode", font=('Georgia', 18),
                              bg="green", fg="white", width=15, height=3, command=encode)
    buttonencode.place(relx=0.4, rely=0.7)

def open_decode(stegno):
    stegno.title('STEGNOGRAPHY APP')
    stegno.geometry("900x500")
    image_path = "D:/virtual studio code/PYTHON/STEGANOGRAPHY/stegano1.png"
    image = Image.open(image_path)
    photo_image = ImageTk.PhotoImage(image)

    bg_image = tk.Label(stegno, image=photo_image)
    bg_image.photo = photo_image  
    bg_image.place(relheight=1, relwidth=1)

    text_label = tk.Label(stegno, text='WELCOME TO STEGANOGRAPHY', font=('Georgia', 30),
                           fg="brown", background="cadetblue")
    text_label.pack()

    def openfile():
        global fileopen
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetype=(("png file", "*.png"), ("all file", "*.*")))

    def decode():
        try:
            message = lsb.reveal(fileopen)
            label4 = tk.Label(text=message)
            label4.place(relx=0.3, rely=0.3)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    buttonselect = tk.Button(stegno, text="Select File", font=('Georgia', 10),
                              bg="green", fg="white", width=15, height=3, command=openfile)
    buttonselect.place(relx=0.1, rely=0.3)

    buttondecode = tk.Button(stegno, text="Decode", font=('Georgia', 18),
                              bg="green", fg="white", width=15, height=3, command=decode)
    buttondecode.place(relx=0.4, rely=0.5)

def main():
    stegno = tk.Tk()
    stegno.title('STEGNOGRAPHY APP')
    stegno.geometry("900x500")

    image_path = "D:/virtual studio code/PYTHON/STEGANOGRAPHY/stegano1.png"
    image = Image.open(image_path)
    photo_image = ImageTk.PhotoImage(image)

    bg_image = tk.Label(stegno, image=photo_image)
    bg_image.photo = photo_image  
    bg_image.place(relheight=1, relwidth=1)

    text_label = tk.Label(stegno, text='WELCOME TO STEGANOGRAPHY', font=('Georgia', 30),
                           fg="brown", background="cadetblue")
    text_label.pack()

    encodeb = tk.Button(stegno, text="Encode", font=('Georgia', 18), 
                        bg="green", fg="white", width=10, height=3, command=lambda: open_encode(stegno))
    encodeb.place(relx=0.3, rely=0.3)

    decodeb = tk.Button(stegno, text="Decode", font=('Georgia', 18),
                         bg="green", fg="white", width=10, height=3, command=lambda: open_decode(stegno))
    decodeb.place(relx=0.5, rely=0.3)

    stegno.mainloop()

if __name__ == "__main__":
    main()
