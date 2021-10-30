from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x900")
        self.root.title("Student Management System")

        # title label
        title_lbl = Label(self.root, text="Face Recognition", font=("ubuntu", 40, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1500, height=60)

        # background image
        bg_img_top = Image.open("images/img8.jpg")
        bg_img_top = bg_img_top.resize((700, 840), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(bg_img_top)

        bg_lbl1 = Label(self.root, image=self.photoimg1)
        bg_lbl1.place(x=0, y=60, width=700, height=840)

        # background image
        bg_img_down = Image.open("images/img4.jpeg")
        bg_img_down = bg_img_down.resize((800, 840), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(bg_img_down)

        bg_lbl2 = Label(self.root, image=self.photoimg2)
        bg_lbl2.place(x=700, y=60, width=800, height=840)

        # button
        b1_1 = Button(bg_lbl2, text="Face Recognition", command=self.face_recog, font=("ubuntu", 20, "bold"), bg="pink", fg="darkblue", cursor="hand2")
        b1_1.place(x=120, y=700, width=250, height=50)

    # =========================== attendance ================================
    def attendance(self,i,r,n,d):
        with open("student.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split((","))
                nameList.append(entry[0])
            if ((i not in nameList) and (r not in nameList) and (n not in nameList) and (d not in nameList)):
                now = datetime.now()
                d1 = now.strftime("%d-%m-%Y")
                dat = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dat},{d1},Present")

        f.close()


    # ================= Face recognition ================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor,minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="", database="facial_reg_sys")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT student_name from student where student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("SELECT roll from student where student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("SELECT Dep from student where student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 77:
                    cv2.putText(img, f"{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 2)
                    cv2.putText(img, f"{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 2)
                    cv2.putText(img, f"{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 2)
                    self.attendance(id,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

                coord = [x, y, w, y]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_clip = cv2.VideoCapture(0)
        while True:
            ret, img = video_clip.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_clip.release()
        cv2.destroyAllWindows()



if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
