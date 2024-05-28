import sqlite3
import tkinter as tk

con = sqlite3.connect("D:\\Users\\Jeff Bayhon\\Downloads\\employee_personal_info.db")

import guiclass

window = tk.Tk()
window.title('Login System')
window.geometry('1000x1500')

gui_design2 = guiclass.employee_personal_info()

# PROGRAM THAT WILL TRANSFER DATA FROM GUI TO DATA BASE -------------------------------------------------------------------------------------------------------
class GUI:
    def Transfer_data(self):
        #INSERT
        firstname = self.firstnametxt.get()
        middlename = self.middle_nametxt.get()
        lastname = self.lastnametxt.get()
        suffix = self.suffixttxt.get()
        datebirth = self.datebirthtxt.get()
        gender = self.gendercombobox.get()
        nationality = self.nationalitytxt.get()
        civil_status = self.civilstatuscombobox.get()
        department = self.departmenttxt.get()
        designation = self.designationtxt.get()
        qualified_department = self.qualified_deptxt.get()
        employee_status = self.employee_statustxt.get()
        paydate = self.paydatetxt.get()
        employee_number = self.employee_numbertxt.get()
        contact_no = self.contact_numbertxt.get()
        email = self.emailtxt.get()
        other_social = self.other_social_mediatxt.get()
        social_id = self.social_media_accounttxt.get()
        add_line1 = self.add_line1txt.get()
        add_line2 = self.add_line2txt.get()
        city_municipality = self.citytxt.get()
        country = self.countrytxt.get()
        state_province = self.state_provincetxt.get()
        zipcode = self.zipcodetxt.get()
        pic_path = self.picture_pathtxt.get()


    # 4 Queries for the 4 tables/frames -------------------------------------------------------------------------------------------------------------------------------------------------

        #INSERT
        query1 = """INSERT INTO basic_info (first_name, middle_name, last_name, suffix, date_of_birth, gender, nationality, civil_status, 
        department, designation, qualified_department, employee_status, paydate, employee_number) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        query2 = """INSERT INTO contact_info (contact_no, email, other_social, social_id) VALUES(?,?,?,?)"""
        query3 = """INSERT INTO address (address_line1, address_line2, city_municipality, country, state_province, zipcode, picture_path) VALUES(?,?,?,?,?,?,?)"""

        query1inp = (firstname, middlename, lastname, suffix, datebirth, gender, nationality, civil_status, department, designation, qualified_department, employee_status, paydate, employee_number)
        query2inp = (contact_no, email, other_social, social_id)
        query3inp = (add_line1, add_line2, city_municipality, country, state_province, zipcode, pic_path)


        con.execute(query1, query1inp)
        con.execute(query2, query2inp)
        con.execute(query3, query3inp)

        con.commit()
        con.close()
        import DATABASE_CLASS_C

        # DELETE
        self.firstnametxt.delete(0,'end')
        self.middle_nametxt.delete(0,'end')
        self.lastnametxt.delete(0,'end')
        self.suffixttxt.delete(0,'end')
        self.datebirthtxt.delete(0,'end')
        self.gendercombobox.delete(0,'end')
        self.nationalitytxt.delete(0,'end')
        self.civilstatuscombobox.delete(0,'end')
        self.departmenttxt.delete(0,'end')
        self.designationtxt.delete(0,'end')
        self.qualified_deptxt.delete(0,'end')
        self.employee_statustxt.delete(0,'end')
        self.paydatetxt.delete(0,'end')
        self.employee_numbertxt.delete(0,'end')
        self.contact_numbertxt.delete(0,'end')
        self.emailtxt.delete(0,'end')
        self.other_social_mediatxt.delete(0,'end')
        self.social_media_accounttxt.delete(0,'end')
        self.add_line1txt.delete(0,'end')
        self.add_line2txt.delete(0,'end')
        self.citytxt.delete(0,'end')
        self.countrytxt.delete(0,'end')
        self.state_provincetxt.delete(0,'end')
        self.zipcodetxt.delete(0,'end')
        self.picture_pathtxt.delete(0,'end')

        print("Data transfered...")


    def create_content(self):
        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        gui_design2 = guiclass.employee_personal_info()
        # Canvas -----------------------------------------------------------------------------------------------------------------
        main_frame = gui_design2.create_canvas(0, 0)

        # Frames -----------------------------------------------------------------------------------------------------------------
        self.frame1 = gui_design2.create_frames(main_frame, 25, 120, 'gray',930, 180)

        self.frame2 = gui_design2.create_frames(main_frame, 25, 320, 'gray',930, 170)

        self.frame3 = gui_design2.create_frames(main_frame, 25, 520, 'gray',930, 150)

        self.frame4 = gui_design2.create_frames(main_frame, 25, 700, 'gray',930, 360)

        #HEADER -----------------------------------------------------------------------------------------------------------------
        titleheading = gui_design2.label2(main_frame,110, 10, 'EMPLOYEE PERSONAL INFORMATION',30, 'bold')

        #FRAME 1 LABEL -----------------------------------------------------------------------------------------------------------------


        self.firstnamelbl = gui_design2.label1(self.frame1,190, 20, 'First Name')
        self.middle_namelbl = gui_design2.label1(self.frame1,340, 20, 'Middle Name')
        self.lastnamelbl = gui_design2.label1(self.frame1,490, 20, 'Last Name')
        self.suffixtlbl = gui_design2.label1(self.frame1,640, 20, 'Suffix')
        self.datebirthlbl = gui_design2.label1(self.frame1,190, 100, 'Date of Birth')
        self.genderlbl = gui_design2.label1(self.frame1,340, 100, 'Gender')
        self.nationalitylbl = gui_design2.label1(self.frame1,490, 100, 'Nationality')
        self.civilstatuslbl = gui_design2.label1(self.frame1,640, 100, 'Civil Status')

        #FRAME 1 TEXTBOX/ENTRY/COMBOBOX
        self.firstnametxt = gui_design2.textbox1(self.frame1,190, 50, 15)
        self.middle_nametxt = gui_design2.textbox1(self.frame1,340, 50, 15)
        self.lastnametxt = gui_design2.textbox1(self.frame1,490, 50, 15)
        self.suffixttxt = gui_design2.textbox1(self.frame1,640, 50, 15)
        self.datebirthtxt = gui_design2.textbox1(self.frame1,190, 130, 15)
        self.gendercombobox = gui_design2.create_combobox(self.frame1,340, 130, ["Male", "Female", "Binary"])
        self.nationalitytxt = gui_design2.create_combobox(self.frame1,490, 130, ["Filipino", "American", "Chinese"])
        self.civilstatuscombobox = gui_design2.create_combobox(self.frame1,640, 130, ["Single", "Married", "Widowed"])


        #FRAME 2 LABEL -----------------------------------------------------------------------------------------------------------------
        self.departmentlbl = gui_design2.label1(self.frame2,40, 10, 'Department')
        self.designationlbl = gui_design2.label1(self.frame2,340, 10, 'Designation')
        self.qualified_deplbl = gui_design2.label1(self.frame2,640, 10, 'Qualified Dependents')
        self.employee_statuslbl = gui_design2.label1(self.frame2,40, 90, 'Employee Status')
        self.paydatelbl = gui_design2.label1(self.frame2,340, 90, 'Paydate')
        self.employee_numberlbl = gui_design2.label1(self.frame2,640, 90, 'Employee Number')

        #FRAME 2 TEXTBOX/ENTRY/COMBOBOX
        self.departmenttxt = gui_design2.textbox1(self.frame2,40, 40, 32)
        self.designationtxt = gui_design2.textbox1(self.frame2,340, 40, 32)
        self.qualified_deptxt = gui_design2.textbox1(self.frame2, 640, 40, 32)
        self.employee_statustxt = gui_design2.create_combobox(self.frame2,40, 120, ['Hired','On Going','Failed'])
        self.paydatetxt = gui_design2.textbox1(self.frame2,340, 120, 32)
        self.employee_numbertxt = gui_design2.textbox1(self.frame2,640, 120, 30)


        #FRAME 3 LABEL -----------------------------------------------------------------------------------------------------------------
        self.contact_infoheading = gui_design2.label2(main_frame,25, 493, 'Contact Info:',12, 'bold')

        self.contact_numberlbl = gui_design2.label1(self.frame3,40, 10, 'Contact No.')
        self.emaillbl = gui_design2.label1(self.frame3,480, 10, 'Email')
        self.other_social_medialbl = gui_design2.label1(self.frame3,40, 80, 'Other(Social Media)')
        self.social_media_accountlbl = gui_design2.label1(self.frame3,480, 80, 'Social Media Account/ID')

        #FRAME 3 TEXTBOX/ENTRY/COMBOBOX

        self.contact_numbertxt = gui_design2.textbox1(self.frame3,40, 40, 47)
        self.emailtxt = gui_design2.textbox1(self.frame3,480, 40, 47)
        self.other_social_mediatxt = gui_design2.create_combobox(self.frame3,40, 110, ['Facebook', 'Twitter', 'Instagram'])
        self.social_media_accounttxt = gui_design2.textbox1(self.frame3,480, 110, 47)

        #FRAME 4 LABEL -----------------------------------------------------------------------------------------------------------------
        self.addressheading = gui_design2.label2(main_frame,25, 675, 'Address:',12, 'bold')

        self.add_line1lbl = gui_design2.label1(self.frame4,40, 10, 'Address Line 1')
        self.add_line2lbl = gui_design2.label1(self.frame4,40, 80, 'Address Line2')
        self.citylbl = gui_design2.label1(self.frame4,40, 150, 'City/Municipality')
        self.state_provincelbl = gui_design2.label1(self.frame4,430, 150, 'State/Province')
        self.countrylbl = gui_design2.label1(self.frame4,40, 220, 'Country')
        self.zipcodelbl = gui_design2.label1(self.frame4,430, 220, 'Zipcode')
        self.picture_pathlbl = gui_design2.label1(self.frame4,40, 290, 'Picture Path')

        #FRAME 4 TEXTBOX/ENTRY/COMBOBOX

        self.add_line1txt = gui_design2.textbox1(self.frame4,40, 40, 90)
        self.add_line2txt = gui_design2.textbox1(self.frame4,40, 110, 90)
        self.citytxt = gui_design2.textbox1(self.frame4,40, 180, 40)
        self.state_provincetxt = gui_design2.textbox1(self.frame4,430, 180, 40)
        self.countrytxt = gui_design2.create_combobox(self.frame4,40, 250, ['Philippines', 'United States', 'China'])
        self.zipcodetxt = gui_design2.textbox1(self.frame4,430, 250, 40)
        self.picture_pathtxt = gui_design2.textbox1(self.frame4,40, 320, 90)

        #PICTURE -----------------------------------------------------------------------------------------------------------------
        # picture = gui_design2.picture(main_frame,50, 80,125,125, 'C:\\Users\\Stan Lee\\Downloads\\Profile.jpg')

        choosebutton = gui_design2.create_button(self.frame1,lambda: self.Transfer_data(),20, 100, 'Choose File', '#AB9C9C',10,1,7)

        self.no_file1lbl = gui_design2.label3(self.frame1,100, 100, 'No File Chosen', 11,1,7, 'bold')

        #BUTTON -----------------------------------------------------------------------------------------------------------------
        self.savebutton = gui_design2.create_button(main_frame,lambda: self.Transfer_data(),25, 1080, 'Save', '#0CC0DF', 12, 2, 8)
        self.cancelbutton = gui_design2.create_button(main_frame,lambda: None,120, 1080, 'Cancel', '#AB9C9C',12,2,8)

        #END PROGRAM
        window.mainloop()
