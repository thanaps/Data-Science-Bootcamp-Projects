# run this one first

class ATM:
    
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password
    
    def check_balance(self):
        message = f"------Account: {self.name}, Balance: {self.balance}------"
        print(message)

    def deposit(self, money):
        if(self.balance >= money):
            self.balance += money
            print(f"New Balance: {self.balance}")
            print("------Deposit successfully.------")
        else:
            print("Insufficient funds in the account")
    def withdraw(self, money):
        if(self.balance >= money):
            self.balance -= money
            print(f"New Balance: {self.balance}")
            print("------Withdraw successfully.------")
        else:
            print("Insufficient funds in the account")
        
    def top_up(self, money):
        if(self.balance >= money):
            self.balance -= money
            number = input("Please specify phone number->")
            print(f"Top-up to {number} successfully")
            print(f"New Balance: {self.balance}")
            print("------Top-up successfully.------")
        else:
            print("Insufficient funds in the account")
        
    def change_name(self, new_acc_name):
        self.name = new_acc_name
        print(f"New account name: {self.name}")
        print("------Your account name has been change.------")
    
    def change_password(self, new_password):
        self.password = new_password
        print(f"New Password: {str(self.password)[:2]}xx")
        print("------Your password has been change.------")
    
    def password_(self):
        return self.password
    def name_(self):
        return self.name
      
     # run this one second

while(True):
    print("What do you want to do at ATM")
    print(" 1. Open an account\n",
        "2. Others\n",
        "3. Exit")
    user_act = input("Press 1 or 2 ->") 

    if(user_act == '1'):
        name = input("Create Name ->") 
        while(True):
                try:
                    balance = int(input("Cash for account ->"))
                    break
                except:
                    print("That's not a valid option!")
        while(True):
            while(True):
                try:
                    password = int(input("Set ATM Password in 4 digits ->"))  
                    break
                except:
                    print("That's not a valid option!")
            if(len(str(password)) == 4):
                break
            else:
                continue
        name = ATM(name, balance, password)
        print("------Open an account Successfull------")

    elif(user_act == '2'):
        print("Please verify your account !!!")
        name_sign = input("Name ->")
        if(name.name_() == name_sign):
            while(True):
                try:
                    pass_sign = int(input("Please type your ATM password ->"))
                    break
                except:
                    print("That's not a valid option!")
            if(pass_sign == name.password_()):
                print("------Login Successfull------")
                select_list = ["check_balance", "deposit", "withdraw", "top_up", "change_name", "change_password"]
                while(True):
                    print("What do you want to do ?")
                    print(" 1. check_balance\n",
                        "2. deposit\n",
                        "3. withdraw\n",
                        "4. top_up\n",
                        "5. change_name\n",
                        "6. change_password\n",
                        "0. Back to home")
                    while(True):
                        try:
                            user_act = int(input("Press 1 to 6 ->"))
                            break
                        except:
                            print("That's not a valid option!")
                    if(user_act == 1 ):
                        print(f"You Select -> {select_list[user_act-1]}")
                        name.check_balance()
                    elif(user_act == 2 ):
                        print(f"You Select -> {select_list[user_act-1]}")
                        while(True):
                            try:
                                dep_sign = int(input("Please specify the amount ->"))
                                break
                            except:
                                print("That's not a valid option!")
                        name.deposit(dep_sign)
                    elif(user_act == 3 ):
                        print(f"You Select -> {select_list[user_act-1]}")
                        while(True):
                            try:
                                with_sign = int(input("Please specify the amount ->"))
                                break
                            except:
                                print("That's not a valid option!")
                        name.withdraw(with_sign)
                    elif(user_act == 4 ):
                        print(f"You Select -> {select_list[user_act-1]}")
                        while(True):
                            try:
                                top_sign = int(input("Please specify the amount ->"))
                                break
                            except:
                                print("That's not a valid option!")
                        name.top_up(top_sign)
                    elif(user_act == 5 ):
                        print(f"You Select -> {select_list[user_act-1]}")
                        new_acc_name = input("Please specify new name ->")
                        name.change_name(new_acc_name)
                    elif(user_act == 6 ):
                        print(f"You Select -> {select_list[user_act-1]}")
                        while(True):
                            while(True):
                                try:
                                    new_pass = int(input("Set ATM Password in 4 digits ->"))  
                                    break
                                except:
                                    print("That's not a valid option!")
                            if(len(str(new_pass)) == 4):
                                break
                            else:
                                continue
                        name.change_password(new_pass)
                    else:
                        break
            else:
                print("------Wrong Password------")
        else:
            print("------Sorry name doesn't exist in the system.------\n------Please Open an account first------")
    else:
        print("------End------")
        break
