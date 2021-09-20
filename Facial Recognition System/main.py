import os, sys, subprocess
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student_Management_System
from train import Train_dataset
from face_recognition import Face_Recognition


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x900")
        self.root.title("Face Recognition System")

        # first image
        img = Image.open("images/pexels-546819.jpg")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=150)

        # second images
        img2 = Image.open("images/mg1.jpeg")
        img2 = img2.resize((500, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=150)

        # third image
        img3 = Image.open("images/imges.jpg")
        img3 = img3.resize((500, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=150)

        # background image
        bg_img = Image.open("images/pexels.jpg")
        bg_img = bg_img.resize((1500, 750), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(bg_img)

        bg_lbl = Label(self.root, image=self.photoimg4)
        bg_lbl.place(x=0, y=150, width=1500, height=750)

        # title label
        title_lbl = Label(bg_lbl, text=" FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE ", font=("ubuntu", 40, "bold"), bg="cyan", fg="red")
        title_lbl.place(x=5, y=5, width=1500, height=45)

        # student button
        img5 = Image.open("images/pexels-2.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_lbl, image=self.photoimg5, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_lbl, text="Student Details", command=self.student_details, font=("ubuntu", 15, "bold"), bg="pink", fg="darkblue", cursor="hand2")
        b1_1.place(x=200, y=300, width=220, height=40)

        # face detector button
        img6 = Image.open("images/img5.jpeg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_lbl, image=self.photoimg6, cursor="hand2", command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_lbl, text="Face Detector", font=("ubuntu", 15, "bold"), bg="pink", fg="darkblue", cursor="hand2", command=self.face_data)
        b1_1.place(x=500, y=300, width=220, height=40)

        # attendance button
        img7 = Image.open("images/img8.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_lbl, image=self.photoimg7, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_lbl, text="Attendance", font=("ubuntu", 15, "bold"), bg="pink", fg="darkblue", cursor="hand2")
        b1_1.place(x=800, y=300, width=220, height=40)

        # help disk button
        img8 = Image.open("images/pexels-thisisengineering-3862622.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_lbl, image=self.photoimg8, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_lbl, text="Help Disk", font=("ubuntu", 15, "bold"), bg="pink", fg="darkblue", cursor="hand2")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # train data button
        img9 = Image.open("images/img4.jpeg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_lbl, image=self.photoimg9, cursor="hand2", command=self.train_data)
        b1.place(x=200, y=400, width=220, height=220)

        b1_1 = Button(bg_lbl, text="Train Data", font=("ubuntu", 15, "bold"), bg="pink", fg="darkblue", cursor="hand2", command=self.train_data)
        b1_1.place(x=200, y=600, width=220, height=40)

        # photos button
        img10 = Image.open("images/img10.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_lbl, image=self.photoimg10, cursor="hand2", command=self.open_images)
        b1.place(x=500, y=400, width=220, height=220)

        b1_1 = Button(bg_lbl, text="Photos", command=self.open_images, font=("ubuntu", 15, "bold"), bg="pink", fg="darkblue", cursor="hand2")
        b1_1.place(x=500, y=600, width=220, height=40)

        # developer button
        img11 = Image.open("images/pexels-christina-morillo-1181341.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_lbl, image=self.photoimg11, cursor="hand2")
        b1.place(x=800, y=400, width=220, height=220)

        b1_1 = Button(bg_lbl, text="Developer", font=("ubuntu", 15, "bold"), bg="pink", fg="darkblue", cursor="hand2")
        b1_1.place(x=800, y=600, width=220, height=40)

        # exit button
        img12 = Image.open("images/img2.jpeg")
        img12 = img12.resize((220, 220), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_lbl, image=self.photoimg12, command=root.quit, cursor="hand2")
        b1.place(x=1100, y=400, width=220, height=220)

        b1_1 = Button(bg_lbl, text="Exit", command=root.quit, font=("ubuntu", 15, "bold"), bg="pink", fg="darkblue", cursor="hand2")
        b1_1.place(x=1100, y=600, width=220, height=40)

    # ======================== Function Button ========================
    def open_images(self):
        if sys.platform == "win32":
            os.startfile("Data")
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "Data"])

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student_Management_System(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train_dataset(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)


if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

