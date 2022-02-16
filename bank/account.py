import time
import os
from .db import *

class Account:
    def option(self):
        print("Which account balance you want to check?\n[1] Current.\n[2] Savings.\n[3] Salary.\n[4] Credit.\n[0] Back")
        ans=int(input("-> "))
        if ans==1:
            return 1
        elif ans==2:
            return 2
        elif ans==3:
            return 3
        elif ans==4:
            return 4
        else:
            return 0
    def curr_acc(self,no):
        os.system("cls")
        mycursor.execute("select amount from current_account where Account_num=(%s)",(no,))
        amt=str(mycursor.fetchone())
        if amt=="None":
            print("You don't have a current account. Would you like to open it?(Y/N)")
            ans=str(input("-> "))
            if( ans[0]=="Y" or ans[0]=="y"):
                print("How much would you like to add in your current account?")
                ans=int(input("-> "))
                mycursor.execute("insert into current_account(Account_num, amount) values(%s,%s)",(no,ans,))
                mydb.commit()
        else:
            raw_text = u"\u20B9"
            size=len(amt)
            print(f"Your current account is having {raw_text}{amt[1:size-2]}")
        time.sleep(10)

    def savings_acc(self,no):
        os.system("cls")
        mycursor.execute("select amount from savings_account where Account_num=(%s)",(no,))
        amt=str(mycursor.fetchone())
        mycursor.execute("select interest from savings_account where Account_num=(%s)",(no,))
        interest=str(mycursor.fetchone())
        if amt=="None":
            print("You don't have a savings account. Would you like to open it?(Y/N)")
            ans=str(input("-> "))
            if( ans[0]=="Y" or ans[0]=="y"):
                print("How much would you like to add in your savings account?")
                ans=int(input("-> "))
                mycursor.execute("insert into savings_account(Account_num, amount,interest) values(%s,%s,7)",(no,ans,))
                mydb.commit()
        else:
            raw_text = u"\u20B9"
            size=len(amt)
            size1=len(interest)
            print(f"Your savings account is having {raw_text}{amt[1:size-2]} and an interest rate of {interest[1:size1-2]}%")
        time.sleep(10)

    def salary_acc(self,no):
        os.system("cls")
        mycursor.execute("select amount from salary_account where Account_num=(%s)",(no,))
        amt=str(mycursor.fetchone())
        if amt=="None":
            print("You don't have a salary account. Would you like to open it?(Y/N)")
            ans=str(input("-> "))
            if( ans[0]=="Y" or ans[0]=="y"):
                print("How much would you like to add in your salary account?")
                ans=int(input("-> "))
                mycursor.execute("insert into salary_account(Account_num, amount) values(%s,%s)",(no,ans,))
                mydb.commit()
        else:
            raw_text = u"\u20B9"
            size=len(amt)
            amt=amt[1:size-2]
            print(f"Your salary account is having {raw_text}{amt}")
        time.sleep(10)
    
    def credit_acc(self,no):
        os.system("cls")
        mycursor.execute("select limit_ from credit_account where Account_num=(%s)",(no,))
        amt=str(mycursor.fetchone())
        mycursor.execute("select used from credit_account where Account_num=(%s)",(no,))
        used=str(mycursor.fetchone())
        raw_text = u"\u20B9"
        if amt=="None":
            print("You don't have a credit account. Would you like to open it?(Y/N)")
            ans=str(input("-> "))
            if( ans[0]=="Y" or ans[0]=="y"):
                print(f"How much limit would you like to add to your credit account?\n[1] {raw_text}60000\n[2] {raw_text}80000\n[3] {raw_text}100000\n[4] {raw_text}150000")
                ans=int(input("-> "))
                if ans==1:
                    ans=60000
                elif ans==2:
                    ans=80000
                elif ans==3:
                    ans=100000
                elif ans==4:
                    ans=150000
                used=0
                mycursor.execute("insert into credit_account(Account_num,limit_,used) values(%s,%s,%s)",(no,ans,used,))
                mydb.commit()
        else:
            size=len(amt)
            amt=amt[1:size-2]
            size=len(used)
            used=used[1:size-2]
            print(f"You have used {raw_text}{used} out of {raw_text}{amt} from your credit account this month")
        time.sleep(10)