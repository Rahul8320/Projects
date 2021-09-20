from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student_Management_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x900")
        self.root.title("Student Management System")

        # ==================== Variables ===============================================
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_course = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_reg = StringVar()
        self.var_roll = StringVar()
        self.var_gen = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_ph = StringVar()
        self.var_add = StringVar()
        self.var_pin = StringVar()
        self.var_tec_id = StringVar()
        self.var_tec_name = StringVar()
        self.var_pro_name = StringVar()
        self.var_pro_code = StringVar()

        # first image
        img = Image.open("images/pexels-546819.jpg")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=150)

        # second images
        img2 = Image.open("images/mg1.jpeg")
        img2 = img2.resize((500, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
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
        title_lbl = Label(bg_lbl, text=" STUDENT MANAGEMENT SYSTEM SOFTWARE ", font=("ubuntu", 40, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=5, y=5, width=1500, height=45)

        # ~~~~~~~~~~~~~~~~~~~~~~~ main frame ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
        main_frame = Frame(bg_lbl, bd=2)
        main_frame.place(x=14, y=60, width=1470, height=680)

        # ***************************** left Label Frame *********************************************
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("Times New Roman", 15, "bold"))
        left_frame.place(x=10, y=10, width=715, height=650)

        # ======================== Current Course Details Label Frame =====================================
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current Course Details", font=("Times New Roman", 13, "bold"))
        current_course_frame.place(x=5, y=30, width=700, height=100)

        # department Label
        dep_label = Label(current_course_frame, text="Department", font=("Times New Roman", 13, "bold"))
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        # department Combo box
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("Times New Roman", 13, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science", "Mechanical", "Electrical", "Information Technology", "Civil", "Electronics")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # course Label
        course_label = Label(current_course_frame, text="Course", font=("Times New Roman", 13, "bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        # course Combo box
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("Times New Roman", 13, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "B.Tech", "M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # year Label
        year_label = Label(current_course_frame, text="Year", font=("Times New Roman", 13, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        # year Combo box
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("Times New Roman", 13, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "1st year", "2nd year", "3rd year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # semester Label
        sem_label = Label(current_course_frame, text="Semester", font=("Times New Roman", 13, "bold"))
        sem_label.grid(row=1, column=2, padx=10, sticky=W)

        # semester Combo box
        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=("Times New Roman", 13, "bold"), state="readonly")
        sem_combo["values"] = ("Select Semester", "1st Semester", "2nd Semester")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # ============================ Student Information Label Frame ====================================
        class_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Student Information", font=("Times New Roman", 13, "bold"))
        class_frame.place(x=5, y=150, width=700, height=450)

        # student id Label
        student_id = Label(class_frame, text="Student ID", font=("Times New Roman", 13, "bold"))
        student_id.grid(row=0, column=0, padx=10, sticky=W)

        # student id entry
        student_id_entry = ttk.Entry(class_frame, textvariable=self.var_std_id, width=20, font=("Times New Roman", 13, "bold"))
        student_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # student name Label
        student_name = Label(class_frame, text="Student Name", font=("Times New Roman", 13, "bold"))
        student_name.grid(row=0, column=2, padx=10, sticky=W)

        # student name entry
        student_name_entry = ttk.Entry(class_frame, textvariable=self.var_std_name, width=20, font=("Times New Roman", 13, "bold"))
        student_name_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # reg no Label
        reg_no = Label(class_frame, text="Registration No", font=("Times New Roman", 13, "bold"))
        reg_no.grid(row=1, column=0, padx=10, sticky=W)

        # reg no entry
        reg_no_entry = ttk.Entry(class_frame, textvariable=self.var_reg, width=20, font=("Times New Roman", 13, "bold"))
        reg_no_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # roll no Label
        roll_no = Label(class_frame, text="Roll No", font=("Times New Roman", 13, "bold"))
        roll_no.grid(row=1, column=2, padx=10, sticky=W)

        # roll no entry
        roll_no_entry = ttk.Entry(class_frame, textvariable=self.var_roll, width=20, font=("Times New Roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # gender Label
        gender = Label(class_frame, text="Gender", font=("Times New Roman", 13, "bold"))
        gender.grid(row=2, column=0, padx=10, sticky=W)

        # gender entry
        # gender_entry = ttk.Entry(class_frame, textvariable=self.var_gen, width=20, font=("Times New Roman", 13, "bold"))
        gender_combo = ttk.Combobox(class_frame, textvariable=self.var_gen, font=("Times New Roman", 13, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB Label
        dob = Label(class_frame, text="DOB", font=("Times New Roman", 13, "bold"))
        dob.grid(row=2, column=2, padx=10, sticky=W)

        # DOB entry
        dob_entry = ttk.Entry(class_frame, textvariable=self.var_dob, width=20, font=("Times New Roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # email ID Label
        email_id = Label(class_frame, text="Email ID", font=("Times New Roman", 13, "bold"))
        email_id.grid(row=3, column=0, padx=10, sticky=W)

        # email ID entry
        email_id_entry = ttk.Entry(class_frame, textvariable=self.var_email, width=20, font=("Times New Roman", 13, "bold"))
        email_id_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # phone no Label
        phone_no = Label(class_frame, text="Phone No", font=("Times New Roman", 13, "bold"))
        phone_no.grid(row=3, column=2, padx=10, sticky=W)

        # phone no entry
        phone_no_entry = ttk.Entry(class_frame, textvariable=self.var_ph, width=20, font=("Times New Roman", 13, "bold"))
        phone_no_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # address Label
        address = Label(class_frame, text="Address", font=("Times New Roman", 13, "bold"))
        address.grid(row=4, column=0, padx=10, sticky=W)

        # address entry
        address_entry = ttk.Entry(class_frame, textvariable=self.var_add, width=20, font=("Times New Roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # pin Label
        pin = Label(class_frame, text="Pin", font=("Times New Roman", 13, "bold"))
        pin.grid(row=4, column=2, padx=10, sticky=W)

        # pin entry
        pin_entry = ttk.Entry(class_frame, textvariable=self.var_pin, width=20, font=("Times New Roman", 13, "bold"))
        pin_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        # teacher id Label
        teacher_id = Label(class_frame, text="Teacher ID", font=("Times New Roman", 13, "bold"))
        teacher_id.grid(row=5, column=0, padx=10, sticky=W)

        # teacher id entry
        teacher_id_entry = ttk.Entry(class_frame, textvariable=self.var_tec_id, width=20, font=("Times New Roman", 13, "bold"))
        teacher_id_entry.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        # teacher name Label
        teacher_name = Label(class_frame, text="Teacher Name", font=("Times New Roman", 13, "bold"))
        teacher_name.grid(row=5, column=2, padx=10, sticky=W)

        # teacher name entry
        teacher_name_entry = ttk.Entry(class_frame, textvariable=self.var_tec_name, width=20, font=("Times New Roman", 13, "bold"))
        teacher_name_entry.grid(row=5, column=3, padx=5, pady=5, sticky=W)

        # project name Label
        project_name = Label(class_frame, text="Project Name", font=("Times New Roman", 13, "bold"))
        project_name.grid(row=6, column=0, padx=10, sticky=W)

        # project name entry
        project_name_entry = ttk.Entry(class_frame, textvariable=self.var_pro_name, width=20, font=("Times New Roman", 13, "bold"))
        project_name_entry.grid(row=6, column=1, padx=5, pady=5, sticky=W)

        # project code Label
        project_code = Label(class_frame, text="Project Code", font=("Times New Roman", 13, "bold"))
        project_code.grid(row=6, column=2, padx=10, sticky=W)

        # project code entry
        project_code_entry = ttk.Entry(class_frame, textvariable=self.var_pro_code, width=20, font=("Times New Roman", 13, "bold"))
        project_code_entry.grid(row=6, column=3, padx=5, pady=5, sticky=W)

        # radio button
        self.var_rad1 = StringVar()
        radio_but1 = ttk.Radiobutton(class_frame, text="Take Photo Sample", variable=self.var_rad1, value="Yes")
        radio_but1.grid(row=7, column=0, padx=20, pady=20, columnspan=2)

        # radio button 2
        radio_but2 = ttk.Radiobutton(class_frame, text="No Photo Sample", variable=self.var_rad1, value="No")
        radio_but2.grid(row=7, column=2, padx=20, pady=20, columnspan=2)

        # =============================== Button Frame =================================
        but_frame = Frame(class_frame, bd=2, relief=RIDGE, bg="white")
        but_frame.place(x=5, y=300, width=680, height=100)

        # save button
        save_button = Button(but_frame, text="Save", command=self.add_data, width=15, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        save_button.grid(row=0, column=0, padx=5, pady=5)

        # update button
        update_button = Button(but_frame, text="Update", command=self.update_data, width=15, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        update_button.grid(row=0, column=1, pady=5)

        # delete button
        delete_button = Button(but_frame, text="Delete", command=self.delete_data, width=15, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        delete_button.grid(row=0, column=2, padx=5, pady=5)

        # reset button
        reset_button = Button(but_frame, text="Reset", command=self.reset_data, width=15, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        reset_button.grid(row=0, column=3, pady=5)

        # take_photo button
        take_photo_button = Button(but_frame, text="Take Photo Sample", command=self.generate_data_set, width=32, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        take_photo_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        # update_photo button
        update_photo_button = Button(but_frame, text="Update Photo Sample",command=self.generate_data_set, width=32, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        update_photo_button.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

        # *********************************** right Label Frame **************************************
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("Times New Roman", 15, "bold"))
        right_frame.place(x=740, y=10, width=715, height=650)

        # ============================= Search Frame ==================================
        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search Details", font=("Times New Roman", 13, "bold"))
        search_frame.place(x=5, y=30, width=700, height=150)

        # search by Label
        search_by_label = Label(search_frame, text="Search By:", font=("Times New Roman", 13, "bold"))
        search_by_label.grid(row=0, column=0, padx=5, sticky=W)

        # search by Combo box
        search_by_combo = ttk.Combobox(search_frame, font=("Times New Roman", 13, "bold"), state="readonly", width=13)
        search_by_combo["values"] = ("Select ", "Roll No", "Phone No", "Email ID", "Pin No")
        search_by_combo.current(0)
        search_by_combo.grid(row=0, column=1, pady=5, sticky=W)

        # search by entry
        search_by_entry = ttk.Entry(search_frame, width=20, font=("Times New Roman", 13, "bold"))
        search_by_entry.grid(row=0, column=2, padx=2, pady=5, sticky=W)

        # search button
        search_button = Button(search_frame, text="Search", width=12, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        search_button.grid(row=0, column=3, padx=2, pady=5)

        # show all button
        show_all_button = Button(search_frame, text="Show All", width=11, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        show_all_button.grid(row=0, column=4, pady=5)

        # =============================== Table Frame ===============================
        table_frame = LabelFrame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=200, width=700, height=400)

        # *-*-*-*-*-*-*-*-*-*-*- Scroll Bar *-*-*-*-*-*-*-*-*-*-*-*
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=('dep', 'course', 'year', 'sem', 'id', 'name', 'reg', 'roll', 'gender', 'dob', 'email', 'phone', 'address', 'pin', 'teacher_id', 'teacher_name', 'project_name', 'project_code', 'photo'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('dep', text="Department")
        self.student_table.heading('course', text="Course")
        self.student_table.heading('year', text="Year")
        self.student_table.heading('sem', text="Semester")
        self.student_table.heading('id', text="Student ID")
        self.student_table.heading('name', text="Student Name")
        self.student_table.heading('reg', text="Registration No")
        self.student_table.heading('roll', text="Roll No")
        self.student_table.heading('gender', text="Gender")
        self.student_table.heading('dob', text="DOB")
        self.student_table.heading('email', text="Email ID")
        self.student_table.heading('phone', text="Phone Number")
        self.student_table.heading('address', text="Address")
        self.student_table.heading('pin', text="Pin")
        self.student_table.heading('teacher_id', text="Teacher ID")
        self.student_table.heading('teacher_name', text="Teacher Name")
        self.student_table.heading('project_name', text="Project Name")
        self.student_table.heading('project_code', text="Project Code")
        self.student_table.heading('photo', text="Photo Sample")
        self.student_table["show"] = "headings"

        self.student_table.column('dep', width=150)
        self.student_table.column('course', width=80)
        self.student_table.column('year', width=70)
        self.student_table.column('sem', width=90)
        self.student_table.column('id', width=100)
        self.student_table.column('name', width=120)
        self.student_table.column('reg', width=100)
        self.student_table.column('roll', width=100)
        self.student_table.column('gender', width=70)
        self.student_table.column('dob', width=100)
        self.student_table.column('email', width=200)
        self.student_table.column('phone', width=100)
        self.student_table.column('address', width=200)
        self.student_table.column('pin', width=70)
        self.student_table.column('teacher_id', width=100)
        self.student_table.column('teacher_name', width=120)
        self.student_table.column('project_name', width=200)
        self.student_table.column('project_code', width=100)
        self.student_table.column('photo', width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ===================== Function Declarations =================
    # ----------------- Add Data to database--------------
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_reg.get() == "" or self.var_roll.get() == "" or self.var_gen.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_ph.get() == "" or self.var_add.get() == "" or self.var_pin.get() == "" or self.var_tec_id.get() == "" or self.var_tec_name.get() == "" or self.var_pro_code.get() == "" or self.var_pro_name.get() == "":
            messagebox.showerror("Error", "All Fields are Mandatory!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root@8320", database="facial_reg_sys")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                                            self.var_dep.get(),
                                                                                                                            self.var_course.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_sem.get(),
                                                                                                                            self.var_std_id.get(),
                                                                                                                            self.var_std_name.get(),
                                                                                                                            self.var_reg.get(),
                                                                                                                            self.var_roll.get(),
                                                                                                                            self.var_gen.get(),
                                                                                                                            self.var_dob.get(),
                                                                                                                            self.var_email.get(),
                                                                                                                            self.var_ph.get(),
                                                                                                                            self.var_add.get(),
                                                                                                                            self.var_pin.get(),
                                                                                                                            self.var_tec_id.get(),
                                                                                                                            self.var_tec_name.get(),
                                                                                                                            self.var_pro_name.get(),
                                                                                                                            self.var_pro_code.get(),
                                                                                                                            self.var_rad1.get()
                                                                                                                        ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Upload successful", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", str(es), parent=self.root)

    # -----------Fetch data from Database ---------------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root@8320", database="facial_reg_sys")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0 :
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, value=i)
            conn.commit()
        conn.close()

    # /---------------- get cursor -------------/
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_reg.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gen.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_ph.set(data[11]),
        self.var_add.set(data[12]),
        self.var_pin.set(data[13]),
        self.var_tec_id.set(data[14]),
        self.var_tec_name.set(data[15]),
        self.var_pro_name.set(data[16]),
        self.var_pro_code.set(data[17]),
        self.var_rad1.set(data[18])

    # /-------------------- update data ------------------/
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_reg.get() == "" or self.var_roll.get() == "" or self.var_gen.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_ph.get() == "" or self.var_add.get() == "" or self.var_pin.get() == "" or self.var_tec_id.get() == "" or self.var_tec_name.get() == "" or self.var_pro_code.get() == "" or self.var_pro_name.get() == "":
            messagebox.showerror("Error", "All Fields are Mandatory!", parent=self.root)
        else:
            try:
                ans = messagebox.askyesno("Update Field", "Do you want to update data?", parent=self.root)
                if ans > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root@8320", database="facial_reg_sys")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, course=%s, year=%s, sem=%s, student_name=%s, reg=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, pin=%s, teacher_id=%s, teacher_name=%s, project_name=%s, project_code=%s, photo=%s WHERE student_id=%s", (
                                                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                                                                    self.var_reg.get(),
                                                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                                                    self.var_gen.get(),
                                                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                                                    self.var_ph.get(),
                                                                                                                                                                                                                                                                    self.var_add.get(),
                                                                                                                                                                                                                                                                    self.var_pin.get(),
                                                                                                                                                                                                                                                                    self.var_tec_id.get(),
                                                                                                                                                                                                                                                                    self.var_tec_name.get(),
                                                                                                                                                                                                                                                                    self.var_pro_name.get(),
                                                                                                                                                                                                                                                                    self.var_pro_code.get(),
                                                                                                                                                                                                                                                                    self.var_rad1.get(),
                                                                                                                                                                                                                                                                    self.var_std_id.get()
                    ))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Update successful", parent=self.root)
                else:
                    if not ans:
                        return
            except Exception as e:
                messagebox.showerror("Error", str(e), parent=self.root)

    # /------------- delete data -------------------------/
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student not Found!", parent=self.root)
        else:
            try:
                ans = messagebox.askyesno("Delete", "Do you want to delete data?", parent=self.root)
                if ans > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root@8320", database="facial_reg_sys")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE student_id = %s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Successfully Deleted", parent=self.root)
                else:
                    if not ans:
                        return
            except Exception as e:
                messagebox.showerror("Error", str(e), parent=self.root)

    # /-------------- reset data -----------------/
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_reg.set("")
        self.var_roll.set("")
        self.var_gen.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_ph.set("")
        self.var_add.set("")
        self.var_pin.set("")
        self.var_tec_id.set("")
        self.var_tec_name.set("")
        self.var_pro_name.set("")
        self.var_pro_code.set("")
        self.var_rad1.set("")

    # /----------------- Generate data set -------------------------/
    def generate_data_set(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_reg.get() == "" or self.var_roll.get() == "" or self.var_gen.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_ph.get() == "" or self.var_add.get() == "" or self.var_pin.get() == "" or self.var_tec_id.get() == "" or self.var_tec_name.get() == "" or self.var_pro_code.get() == "" or self.var_pro_name.get() == "":
            messagebox.showerror("Error", "All Fields are Mandatory!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root@8320", database="facial_reg_sys")
                my_cursor = conn.cursor()
                # my_cursor.execute("SELECT * FROM student")
                # result = my_cursor.fetchall()
                id = self.var_std_id.get()
                # for x in result:
                #     id += 1
                my_cursor.execute("update student set Dep=%s, course=%s, year=%s, sem=%s, student_name=%s, reg=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, pin=%s, teacher_id=%s, teacher_name=%s, project_name=%s, project_code=%s, photo=%s WHERE student_id=%s", (
                                                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                                                        self.var_reg.get(),
                                                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                                                        self.var_gen.get(),
                                                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                                                        self.var_ph.get(),
                                                                                                                                                                                                                                                        self.var_add.get(),
                                                                                                                                                                                                                                                        self.var_pin.get(),
                                                                                                                                                                                                                                                        self.var_tec_id.get(),
                                                                                                                                                                                                                                                        self.var_tec_name.get(),
                                                                                                                                                                                                                                                        self.var_pro_name.get(),
                                                                                                                                                                                                                                                        self.var_pro_code.get(),
                                                                                                                                                                                                                                                        self.var_rad1.get(),
                                                                                                                                                                                                                                                        self.var_std_id.get() == id
                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # /--------------------- Load predefined data -------------------------/
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor = 1.3
                    # minimum neighbours =5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed successfully.")

            except Exception as e:
                messagebox.showerror("Error", str(e), parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = Student_Management_System(root)
    root.mainloop()
