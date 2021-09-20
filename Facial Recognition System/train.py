from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train_dataset:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x900")
        self.root.title("Student Management System")

        # title label
        title_lbl = Label(self.root, text="Train Data Set", font=("ubuntu", 40, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1500, height=50)

        # background image
        bg_img_top = Image.open("images/img8.jpg")
        bg_img_top = bg_img_top.resize((1500, 400), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(bg_img_top)

        bg_lbl1 = Label(self.root, image=self.photoimg1)
        bg_lbl1.place(x=0, y=50, width=1500, height=400)

        # button
        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier, font=("ubuntu", 30, "bold"), bg="pink", fg="darkblue", cursor="hand2")
        b1_1.place(x=0, y=450, width=1500, height=50)

        # background image
        bg_img_down = Image.open("images/img4.jpeg")
        bg_img_down = bg_img_down.resize((1500, 400), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(bg_img_down)

        bg_lbl2 = Label(self.root, image=self.photoimg2)
        bg_lbl2.place(x=0, y=500, width=1500, height=400)

    def train_classifier(self):
        data_dir = "Data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') # gray scale convert
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            if cv2.waitKey(1) == 13:
                break

        ids = np.array(ids)

        # =============== Train the classifier ====================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed.")


if __name__ == '__main__':
    root = Tk()
    obj = Train_dataset(root)
    root.mainloop()
