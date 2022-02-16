class Option:
    def option(self):
            print(f"What would you like to do?")
            print("[1] Update Profile.\n[2] Check Balance.\n[3] Change Password.\n[4] Withdraw Cash.\n[5] Deposit money.\n[0] Exit")
            ans=int(input("-> "))
            if ans==1:
                return 1
            elif ans==2:
                return 2
            elif ans==3:
                return 3
            elif ans==4:
                return 4
            elif ans==5:
                return 5
            else:
                return 0
