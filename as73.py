import json
class bank:
    def addconstumer(self):
        self.name = str(input("enter constumer's name:"))
        self.accnum = int(input("enter account name:"))
        self.balance = float(input("enter account balance:"))
        self.pin = int(input("enter your safety pin:"))
        customer={ "name":self.name,"accnum":self.accnum,"balance":self.balance,"pin":self.pin}
        with open("bank.json","a") as f:
             json.dump(customer,f)
             f.write("\n")
    def withdraw(self):
        #count=0
        self.n = int(input("enter accnumber to withdraw cash:"))
        self.pin_in = int(input("enter pin for that account:"))
        with open("bank.json","r") as f:
            data = (f.readlines())
        found = False
        update_data=[]
        for customer_data in customer:
            customer = customer_data.strip()
            if(not customer_data):
                continue
            
            try:
               for customer_data in data:
               customer = json.loads(customer_data.strip())
            except json.JSONDecodeError:
                continue
            #print(customer)
            if(customer["accnum"]==self.n and customer["pin"]==self.pin_in):
                found=True
                print("current balance is",customer["balance"])
                amt = float(input("enter amt to withdraw:"))
                if customer["balance"] <= amt:
                    print("insufficiant balance!")
                else:
                    customer["balance"]-=amt
                update_data.append(customer)
        else:
                update_data.append(customer)
        #update_data = list(customer)
        if found:
            with open("bank.json","a") as f:
             for customer_data in customer:
                 json.dump(customer,f)
                 f.write("\n")
        else :
            print("account not found:")
    def deposite(self):
        self.n = int(input("enter accnumber to deposite cash:"))
        self.pin_in = int(input("enter pin for that account:"))
        with open("bank.json","r") as f:
            data = (f.readlines())
        found = False
        update_data=[]
        for customer_data in data:
            customer = json.load(customer_data.strip())
            if(customer["accnum"]==self.n and customer["pin"]==self.pin_in):
                found=True
                print("current balance is",customer["balance"])
                amt = float(input("enter amt to withdraw:"))
                customer["balance"]+=amt
        update_data.append(customer)
        if found:
            with open("bank.json","a"):
             for customer_data in customer:
                 json.dump(customer,f)
                 f.write("\n")
        else :
            print("account not found:")
        
s=bank()
#s.addconstumer()
#s.addconstumer()
#s.addconstumer()
s.withdraw()    
                
                
                
                
            