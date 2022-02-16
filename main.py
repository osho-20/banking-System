import os
import time
from bank.login import Login
from bank.profile import Profile
from bank.options import Option
from bank.update import Update
from bank.account import Account
from bank.transaction import transaction
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("1 minute to verify details: "+timer, end="\r")
        time.sleep(1)
        t -= 1
    

if __name__ == "__main__":
    os.system('cls')
    welcome = "WELCOME TO MY BANK"
    quote = "Your Need Is Our First Priority"
    welcome = welcome.center(90)
    quote = quote.center(92)
    congo = "CONGRATULATIONS!!! You have created your profile successfully."
    while True:
        os.system("cls")
        print(welcome + "\n" + quote)
        print("What would you like to do?")
        print("[1] Create account.\n[2] Login.\n[3] Loan Schemes.\n[4] What's New?")
        task = int(input("-> "))
        customer = Profile()
        if task == 1:
            customer.create()
            os.system("cls")
            print(congo)
            time.sleep(0.02)
            print("\n")
            customer.display()
            print("\n")
            countdown(60)
        elif task == 2:
            login1=Login()
            status=False
            status=login1.get_values()
            time.sleep(3)
            if status!=False:
                while True:
                    os.system("cls")
                    opt=Option()
                    numb=opt.option()
                    if numb==0:
                        break
                    elif numb==1:
                        while True:
                            os.system("cls")
                            upd=Update()
                            out=upd.opt()
                            if out==0:
                                break
                            elif(out == 1):
                                upd.update_contact(status)
                            elif out ==2:
                                upd.update_email(status)
                            else:
                                upd.update_add(status)
                    elif numb==2:
                        while True:
                            os.system("cls")
                            acc=Account()
                            opt=acc.option()
                            if opt==1:
                                acc.curr_acc(status)
                            elif opt==2:
                                acc.savings_acc(status)
                            elif opt==3:
                                acc.salary_acc(status)
                            elif opt==4:
                                acc.credit_acc(status)
                            else: break
                    elif numb==3:
                        upd=Update()
                        upd.update_pass(status)
                    elif numb==4:
                        remove=transaction()
                        ans=remove.remove()
                        os.system("cls")
                        if ans==1:
                            remove.remove_savings(status)
                        elif ans==2:
                            remove.remove_curr(status)
                        elif ans==3:
                            remove.remove_salary(status)
                    elif numb==5:
                        add=transaction()
                        ans=add.add()
                        os.system("cls")
                        if ans==1:
                            add.add_savings(status)
                        elif ans==2:
                            add.add_curr(status)
                        elif ans==3:
                            add.add_salary(status)

        elif task == 3:
            print("loans")
            time.sleep(5)
        elif task == 4:
            print("Nothing")
            time.sleep(5)
