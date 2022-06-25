class BankAccount:
 interest_rate=0.05
 def __init__(self, name, balance=0):

 self.__name=name
 self.__balance=balance

 def deposit(self, val):
    if val>0 and type(val)==int:
        self.__balance+=val 
    else:
        print("양의 정수값으로 입금액을 입력해주십시오")

def withdraw(self, val):
    if val>0 and type(val)==int:
        if val>self.__balance:
            print("예금 부족!!!")
            return False
        else:
            self.__balance-=val return True
    
    else:
        print("양의 정수값으로 출금액을 입력해주십시오")

def getName(self):
    return self.__name

def getBalance(self):
    return self.__balance

def disp(self):
    print(f"name : {self.__name} \t balance : {self.__balance}")

def calcuInterest(self):
    interest=int(self.__balance*BankAccount.interest_rate)
    self.__balance+=interest
    print("name : {} \t balance : {}". format(self.__name,self.__balance))