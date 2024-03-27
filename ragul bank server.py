#RESERVE BANK

class RBI:
    def __init__(self):
        self.rbiaccount=1000
        self.rbibalance=100000

class SBI(RBI):
    def __init__(self):
        self.sbiaccount=500
        self.sbibalance=20000
        super(). __init__()

class TAMILNADU(SBI,RBI):
    def __init__(self):
        self.tamilnaduaccount=300
        self.tamilnaduaccount=4500
        super(). __init__()

class TRICHY(TAMILNADU,SBI,RBI):
    def __init__(self):
        self.trichyaccount=50
        self.trichybalance=800
        super(). __init__()
    def deposit(self,x):
        self.trichybalance=self.trichybalance+x
        self.tamilnadubalance=self.trichybalance+x
        self.sbibalance=self.sbibalance+x
        self.rbibalance=self.rbibalance+x
        print(self.trichybalance+x)
    def withdraw(self,x):
        self.trichybalance=self.trichybalance-x
        self.tamilnadubalance=self.trichybalance-x
        self.sbibalance=self.sbibalance-x
        self.rbibalance=self.rbibalance-x
        print(self.trichybalance-x)
    def add(self,x):
        self.trichyaccount=self.trichyaccount+x
        self.tamilnaduaccount=self.tamilnaduaccount+x
        self.sbiaccount=self.sbiaccount+x
        self.rbiaccount=self.rbiaccount+x
        print(self.trichyaccount+x)
    def sub(self,x):
        self.trichyaccount=self.trichyaccount-x
        self.tamilnaduaccount=self.tamilnaduaccount-x
        self.sbiaccount=self.sbiaccount-x
        self.rbiaccount=self.rbiaccount-x
        print(self.trichyaccount-x)
   

z=TRICHY()
z.deposit(200)
z.withdraw(10)
z.add(20)
z.sub(40)
s=open(r"C:\Users\ragul\OneDrive\Desktop\bank server.txt","a+")
s.write("bank\n")
s.write("ragul")

A = { "reservebank": [z.rbiaccount, z.rbibalance],
      "statebank": [z.sbiaccount, z.sbibalance],
      "tamilnadu": [z.tamilnaduaccount, z.tamilnadubalance],
      "thirunelveli": [z.trichyaccount, z.trichybalance]
    }

s.write(str(A)+"\n")
s.close()







