import os
import getpass
import random
from .db import *


class Profile:
    def create(self):
        os.system('cls')
        ans = "Y"
        while ans[0] == "Y" or ans[0] == "y":
            print("Enter your Father's name.")
            self.father_name = str(input("-> "))
            print("The entered name is-> " + self.father_name)
            print("Would you like to edit the above detail?(Y/N).")
            ans = input("-> ")
        ans = "Y"

        while ans[0] == "Y" or ans[0] == "y":
            os.system("cls")
            print("Enter your Mother's name.")
            self.mother_name = str(input("-> "))
            print("The entered name is-> " + self.mother_name)
            print("Would you like to edit the above detail?(Y/N).")
            ans = input("-> ")
        ans = "Y"

        while ans[0] == "Y" or ans[0] == "y":
            os.system("cls")
            print("Enter your First name.")
            self.fname = str(input("-> "))
            print("Enter your Last name.")
            self.lname = str(input("-> "))
            print("The entered name is-> " + self.fname + " " + self.lname)
            print("Would you like to edit the above detail?(Y/N).")
            ans = input("-> ")
        ans = "Y"

        while ans[0] == "Y" or ans[0] == "y":
            os.system("cls")
            print("Enter your number of siblings.")
            self.siblings = str(input("-> "))
            print("The entered number is-> " + self.siblings)
            print("Would you like to edit the above detail?(Y/N).")
            ans = input("-> ")
        ans = "Y"

        while ans[0] == "Y" or ans[0] == "y":
            os.system("cls")
            print("Enter your Blood group.")
            self.blood_group = str(input("-> "))
            print("The entered blood group is-> " + self.blood_group)
            print("Would you like to edit the above detail?(Y/N)")
            ans = input("-> ")
        ans = "Y"

        while ans[0] == "Y" or ans[0] == "y":
            os.system("cls")
            print(
                "Enter your Date Of Birth.(DD-MM-YYYY without any special character)."
            )
            self.dob = str(input("-> "))
            error = "na"
            if len(self.dob) != 8:
                error = "E"

            while error == "E":
                os.system("cls")
                print("Above Date Of Birth is wrong please enter correctly.")
                print(
                    "Enter your Date Of Birth.(DD-MM-YYYY without any special character)."
                )
                self.dob =str(input("-> "))
                if len(self.dob) == 8:
                    error = "N"
            self.dob=self.dob[0]+ self.dob[1]+ "-"+ self.dob[2]+ self.dob[3]+ "-"+ self.dob[4]+ self.dob[5] + self.dob[6]+ self.dob[7]
            print("Your entered Date Of Birth is-> "+ self.dob)
            print("Would you like to edit the above detail?(Y/N).")
            ans = input("-> ")
        ans = "Y"

        while ans[0] == "Y" or ans[0] == "y":
            os.system("cls")
            print("Enter your Email account.")
            self.email = str(input("-> "))
            print("The entered email is-> " + self.email)
            print("Would you like to edit the above detail?(Y/N).")
            ans = input("-> ")
        ans = "Y"

        while ans[0] == "Y" or ans[0] == "y":
            os.system("cls")
            print("Enter your contact number.")
            self.contact = str(input("-> "))
            print("The entered contact number is-> " + self.contact)
            print("Would you like to edit the above detail?(Y/N).")
            ans = input("-> ")
        ans = "Y"

        while ans[0] == "Y" or ans[0] == "y":
            os.system("cls")
            print("Enter your House Address.")
            self.address = str(input("-> "))
            print("The entered address is-> " + self.address)
            print("Would you like to edit the above detail?(Y/N).")
            ans = input("-> ")
        ans = "Y"

        while ans[0] == "Y" or ans[0] == "y":
            os.system("cls")
            print("Create a password")
            self.password = str(getpass.getpass("-> "))
            print("Confirm password")
            self.confirm = str(getpass.getpass("-> "))
            while self.password != self.confirm:
                os.system("cls")
                print("password didn't match please re-enter.")
                print("Create a password")
                self.password = str(getpass.getpass("-> "))
                print("Confirm password")
                self.confirm = str(getpass.getpass("-> "))
            break
        self.full_name=self.fname+" "+self.lname
        self.acc_no=random.randint(1e9,1e10-1)
        mycursor.execute("select Account_num from profile where Account_num = (%s)",(self.acc_no,))
        self.no=str(mycursor.fetchone())
        print(self.no)
        while self.no!="None":
            print(self.no)
            self.acc_no=random.randint(1e9,1e10-1)
            mycursor.execute("select Account_num from profile where Account_num = (%s);",(self.acc_no,))
            self.no=str(mycursor.fetchone())
        mycursor.execute("insert into profile(Holder,Father,Mother,Date_of_birth,Siblings,Contact,Email,Address,Account_num) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);",(self.full_name,self.father_name,self.mother_name,self.dob,self.siblings,self.contact,self.email,self.address,self.acc_no,))
        mydb.commit()
        mycursor.execute("insert into login(Account_num,Password) values(%s,%s);",(self.acc_no,self.password,))
        mydb.commit()

    def display(self):
        print(
            "Account Holder Name: "
            + self.full_name
            + "\n"
            +"Account Number: "
            + str(self.acc_no)
            + "\n"
            + "Father's Name: "
            + self.father_name
            + "\n"
            + "Mother's Name: "
            + self.mother_name
            + "\n"
            + "Blood Group: "
            + self.blood_group
            + "\n"
            + "Contact detail's: "
            + self.contact
            + " "
            + self.email
            + "\n"
            + "Address: "
            + self.address
            + "\n"
        )
