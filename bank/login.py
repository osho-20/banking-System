import os 
import time
import getpass
from .db import *
class Login:
    def get_values(self):
        print("Please Enter your Account number to login: ")
        self.no=input("-> ")
        mycursor.execute("select Password from login where Account_num= (%s);",(self.no,))
        self.con=str(mycursor.fetchone())
        size=len(self.con)
        self.con=self.con[2:size-3]
        if self.con=="None":
            print("No Account is found with that account number.")
            time.sleep(6)
            return False
        n=3
        while True:
            if n==0:
                return False
            print(f"Please Enter Your PASSWORD: ({n} attempts left)")
            self.pas=str(getpass.getpass("-> "))
            self.pas=self.pas
            if self.pas==self.con:
                os.system('cls')
                mycursor.execute("select Holder from profile where Account_num=(%s)",(self.no,))
                self.name=str(mycursor.fetchone())
                size=len(self.name)
                print("Hi "+self.name[2:size-3]+". You have logged into your account Successfully")
                time.sleep(1)
                return self.no
            else:
                os.system('cls')
                print("Sorry! The password is incorrect")
                n=n-1

    # def update_contact(self):
    #     ans = "Y"
    #     while ans[0] == "Y" or ans[0] == "y":
    #         os.system("cls")
    #         print("Enter your contact number.")
    #         self.con = input("-> ")
    #         print("The entered contact number is-> " + self.con)
    #         print("Would you like to edit the above detail?(Y/N).")
    #         ans = input("-> ")
    #     mycursor.execute("update profile set contact= (%s) where Account_num= (%s);",(self.con,self.no,))
    #     mydb.commit()
    
    # def option(self):
    #     size=len(self.name)
    #     while True:
    #         print(f"What would you like to do {self.name[2:size-3]}?")
    #         print("[1] Update Profile.\n[2] Check Balance.\n[3] Change Password.\n[4] Withdraw Cash.\n[5] Deposit money.\n[0] Exit")
    #         ans=int(input("-> "))
    #         if ans==1:
    #             while True:
    #                 print("What would you like to update in your profile?\n[1] Phone Number.\n[2] Email Address.\n[3] Home Address.\n[0] Back.")
    #                 up=int(input("-> "))
    #                 if up==1:
    #                     self.update_contact()
    #         elif ans==2:
    #             print()
    #         elif ans==3:
    #             print()
    #         elif ans==4:
    #             print()
    #         else:
    #             return
