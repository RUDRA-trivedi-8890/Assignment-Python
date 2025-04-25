class password_manager:
    old_pass=[]
    @classmethod
    def get_password(self):
        print("the current password is:")
        print(self.old_pass[-1])
    def set_password(self):
        s=str(input("set a password:"))
        if(s not in self.old_pass):
            self.old_pass.append(s)
    def is_correct(self,s):
        if(s==self.old_pass[-1]):
            return True
        else:
            return False
s=password_manager()
print("enter 1 for Know current password")
print("enter 2 for set password:")
print("enter 3 for verify user:")
n = int(input())
if(n==1):
    s.get_password()
elif(n==2):
    s.set_password()
else:
    s.is_correct()