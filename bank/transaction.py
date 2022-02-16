import time
import os
from .db import *
class transaction:
    def remove(self):
        print("From which account would you like to withdraw?\n[1] Savings.\n[2] Current.\n[3] Salary")
        ans=int(input("-> "))
        if(ans<=3 and ans>=1):
            return ans
    def add(self):
        print("In which account would you like to deposit?\n[1] Savings.\n[2] Current.\n[3] Salary")
        ans=int(input("-> "))
        if(ans<=3 and ans>=1):
            return ans

    def remove_curr(self,no):
        mycursor.execute("select amount from current_account where Account_num=(%s)",(no,))
        amt=str(mycursor.fetchone())
        if amt=="None":
            print("Please check your balance.")
            time.sleep(5)
            return
        print("how much would you like to withdraw?")
        size=len(amt)
        amt=amt[1:size-2]
        amt=int(amt)
        amt1=int(input("-> "))
        # print(amt,amt1)
        if(amt1>amt):
            os.system("cls")
            print("Insufficient Balance.")
            time.sleep(5)
            return
        else:
            os.system("cls")
            amt=amt-amt1
            mycursor.execute("update current_account set amount= (%s) where Account_num= (%s);",(amt,no,))
            mydb.commit()
            print("Transaction Successful")
            time.sleep(5)
            return
    def add_curr(self,no):
        mycursor.execute("select amount from current_account where Account_num=(%s)",(no,))
        amt=str(mycursor.fetchone())
        if amt=="None":
            print("Please check your balance.")
            time.sleep(5)
            return
        print("how much would you like to deposit?")
        size=len(amt)
        amt=amt[1:size-2]
        amt=int(amt)
        amt1=int(input("-> "))
        os.system("cls")
        amt=amt+amt1
        mycursor.execute("update current_account set amount= (%s) where Account_num= (%s);",(amt,no,))
        mydb.commit()
        print("Transaction Successful")
        time.sleep(5)
        return
    
    def remove_savings(self,no):
        mycursor.execute("select amount from savings_account where Account_num=(%s)",(no,))
        amt=str(mycursor.fetchone())
        if amt=="None":
            print("Please check your balance.")
            time.sleep(5)
            return
        print("how much would you like to withdraw?")
        size=len(amt)
        amt=amt[1:size-2]
        amt=int(amt)
        amt1=int(input("-> "))
        # print(amt,amt1)
        if(amt1>amt):
            os.system("cls")
            print("Insufficient Balance.")
            time.sleep(5)
            return
        else:
            os.system("cls")
            amt=amt-amt1
            mycursor.execute("update savings_account set amount= (%s) where Account_num= (%s);",(amt,no,))
            mydb.commit()
            print("Transaction Successful")
            time.sleep(5)
            return
    
    def add_savings(self,no):
        mycursor.execute("select amount from savings_account where Account_num=(%s)",(no,))
        amt=str(mycursor.fetchone())
        if amt=="None":
            print("Please check your balance.")
            time.sleep(5)
            return
        print("how much would you like to deposit?")
        size=len(amt)
        amt=amt[1:size-2]
        amt=int(amt)
        amt1=int(input("-> "))
        os.system("cls")
        amt=amt+amt1
        mycursor.execute("update savings_account set amount= (%s) where Account_num= (%s);",(amt,no,))
        mydb.commit()
        print("Transaction Successful")
        time.sleep(5)
        return

    def remove_salary(self,no):
        mycursor.execute("select amount from salary_account where Account_num=(%s)",(no,))
        amt=str(mycursor.fetchone())
        if amt=="None":
            print("Please check your balance.")
            time.sleep(5)
            return
        print("how much would you like to withdraw?")
        size=len(amt)
        amt=amt[1:size-2]
        amt=int(amt)
        amt1=int(input("-> "))
        # print(amt,amt1)
        if(amt1>amt):
            os.system("cls")
            print("Insufficient Balance.")
            time.sleep(5)
            return
        else:
            os.system("cls")
            amt=amt-amt1
            mycursor.execute("update salary_account set amount= (%s) where Account_num= (%s);",(amt,no,))
            mydb.commit()
            print("Transaction Successful")
            time.sleep(5)
            return

    def add_salary(self,no):
        mycursor.execute("select amount from salary_account where Account_num=(%s)",(no,))
        amt=str(mycursor.fetchone())
        if amt=="None":
            print("Please check your balance.")
            time.sleep(5)
            return
        print("how much would you like to deposit?")
        size=len(amt)
        amt=amt[1:size-2]
        amt=int(amt)
        amt1=int(input("-> "))
        os.system("cls")
        amt=amt+amt1
        mycursor.execute("update salary_account set amount= (%s) where Account_num= (%s);",(amt,no,))
        mydb.commit()
        print("Transaction Successful")
        time.sleep(5)
        return