from .db import *
import os
import time
import getpass
class Update:
    def opt(self):
            print("What would you like to update in your profile?\n[1] Phone Number.\n[2] Email Address.\n[3] Home Address.\n[0] Back.")
            up=int(input("-> "))
            if up==1:
                return 1
            elif up==2:
                return 2
            elif up==3:
                return 3
            else :
                return 0
    def update_contact(self,no):
        ans = "Y"
        while ans[0] == "Y" or ans[0] == "y":
            os.system("cls")
            print("Enter your New contact number.")
            self.con = input("-> ")
            print("The entered contact number is-> " + self.con)
            print("Would you like to edit the above detail?(Y/N).")
            ans = input("-> ")
        mycursor.execute("update profile set contact= (%s) where Account_num= (%s);",(self.con,no,))
        mydb.commit()
        print("Your Contact number is successfully updated.")
        time.sleep(5)
        return
    def update_email(self,no):
        ans = "Y"
        while ans[0] == "Y" or ans[0] == "y":
            os.system("cls")
            print("Enter your  New email Address.")
            self.eml = str(input("-> "))
            print("The entered Email adress is-> " + self.eml)
            print("Would you like to edit the above detail?(Y/N).")
            ans = input("-> ")
        mycursor.execute("update profile set Email= (%s) where Account_num= (%s);",(self.eml,no,))
        mydb.commit()
        print("Your Email is successfully updated.")
        time.sleep(5)
        return
    def update_add(self,no):
        ans = "Y"
        while ans[0] == "Y" or ans[0] == "y":
            os.system("cls")
            print("Enter your New House Address.")
            self.add = str(input("-> "))
            print("The entered adress is-> " + self.add)
            print("Would you like to edit the above detail?(Y/N).")
            ans = input("-> ")
        mycursor.execute("update profile set Address= (%s) where Account_num= (%s);",(self.add,no,))
        mydb.commit()
        print("Your Address is successfully updated.")
        time.sleep(5)
        return
    def update_pass(self,no):
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
        mycursor.execute("update login set Password= (%s) where Account_num= (%s);",(self.password,no,))
        mydb.commit()
        print("Your Password is successfully updated.")
        time.sleep(5)
        return