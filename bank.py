# Super class Bank
class Bank(object):
    def __init__(self, BankId, Bankname, Location):
        self.BankId = BankId
        self.Bankname = Bankname
        self.Location = Location



class Customer(Bank):
    def __init__(self,BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo):

        super(Customer, self).__init__(BankId, Bankname, Location)
        self.accounts = {}
        self.CustomerId = CustomerId
        self.AcctNo = AccountNo
        self.Name = Name
        self.Address = Address
        self.PhoneNo = PhoneNo

        self.accounts.update({CustomerId:{'CustomerId':self.CustomerId, 'Name':self.Name, 'Address':self.Address, 'PhoneNo':self.PhoneNo, self.AcctNo:{'accountNumber':self.AcctNo, 'AccountBalance':0}}})

# Method to return details on the customer stored in dictionary called self.accounts
    def GeneralInquiry(self):
        try:
            x = self.accounts[self.CustomerId]['CustomerId']
            y = self.accounts[self.CustomerId]['Name']
            z = self.accounts[self.CustomerId]['Address']
            p = self.accounts[self.CustomerId]['PhoneNo']
            r = self.accounts[self.CustomerId][self.AcctNo]['accountNumber']
            n = self.accounts[self.CustomerId][self.AcctNo]['AccountBalance']
            print('Bank ID:%s\nBank Name: %s\nBank Location: %s\n' % (self.BankId, self.Bankname, self.Location))
            print('CustomerId: %s\nCustomer_Name: %s\nAddress: %s\nPhoneNo.: %s \n' % (x, y, z, p))
            print('AccountNo: %s\nAccountBalance: %s\n' % (r, n))

            try:
                v = self.accounts[self.CustomerId]['loan']['loanbalance']
                f = self.accounts[self.CustomerId]['loan']['loanType']
                print('Active_Loan: %s\n' % v)
                print('loan Type: %s\n' % f)
            except:
                print('Loan not activated for this Account')
        except:
            print('Account does not exist!')

# Method to allow additon or increment on Customer of value in Accouunt Balance

    def DepositMoney(self, Amount):
        self.Amount = Amount
        if self.Amount > 0:
            self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] += self.Amount
# method to allow decrement of value in Account Balance

    def WithdrawMoney(self, amount):
        # Test to for amount to withdrawn
        self.amount = amount
        if 0 < self.amount < self.accounts[self.CustomerId][self.AcctNo]['AccountBalance']:
            self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] -= self.amount
        else:
            print('Insufficient balance')

 # Method to  create dictionary where the data of the customer is stored in the dictionary

    def OpenAccount(self):
        self.accounts[self.CustomerId] = {}
        self.accounts[self.CustomerId]['Name'] = self.Name
        self.accounts[self.CustomerId]['CustomerId'] = self.CustomerId
        self.accounts[self.CustomerId]['Address'] = self.Address
        self.accounts[self.CustomerId]['PhoneNo'] = self.PhoneNo
        self.accounts[self.CustomerId][self.AcctNo] = {}
        self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] = 0
        return self.accounts

# DELETING ACCOUNT

    def CloseAccount(self):
        del self.accounts[self.CustomerId]
        
# APPLYING FOR LOAN

    def ApplyForLoan(self, loanAmount):
        self.loanAmount = loanAmount
        try:
            self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        except:
            print('Your are not eligible for a loan')
        if self.loanAmount > (1.5 * (self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'])):
            print('Your not eligible')
        else:
            print('Request Successful')

    def RequestCard(self):
        
        try:
            self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
            print("Card requested")
        except:
            print('Your are not eligible for Card please create an account first!')




class Teller(Customer, Bank):
    def __init__(self,TellerId, BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo):
    
        super(Teller, self).__init__(BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo)
        self.TellerId = TellerId
        try:
            self.Teller = {1: {'teller_Name': 'pather', 'Id': 1}, 2: {'teller_Name': 'arnold', 'Id': 2},
                           3: {'teller_Name': 'picho', 'Id': 3}}
            self.TellerId = self.Teller[self.TellerId]['Id']
        except:
            print('enter right teller Id')



    def CollectMoney(self):
        if self.Amount > 0:
            self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] += self.Amount
        else:
            print('ENTER AMMOUNT TO WITHDRAW')

    def LoanRequest(self, loanId, Type):
        self.loanType = Type
        self.loanId = loanId
        
        try:
            self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        except:
            print('Your are not eligible for a loan')
        if self.loanAmount > (1.5*(self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'])):
            print('Your not eligible')
        else:
            self.accounts[self.CustomerId]['loan'] = {}
            self.accounts[self.CustomerId]['loan']['loanId'] = self.loanId
            self.accounts[self.CustomerId]['loan']['loanType'] = self.loanType
            self.accounts[self.CustomerId]['loan']['loanbalance'] = -self.loanAmount
            print('loan account has been created!')

    def ProvideInfo(self):
        try:

           print('Bank ID:%s\nBank Name: %s\nBank Location: %s\n' % (self.BankId, self.Bankname, self.Location))
           print('Teller Id: %s\nTeller Name: %s\n' % (self.Teller[self.TellerId]['Id'], self.Teller[self.TellerId]['teller_Name']))
        except:
            print('TellerId not recognised')

    def IssueCard(self):
        if self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] == self.AcctNo:
            print('Your request  for card was received and your Card is ready')
        else:
            print('Not eligible for card issuing')


class Account(Customer):
    pass


class Loan(Customer):

    def __init__(self, LoanId, Type, AccountId, BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo):
        super(Loan, self).__init__(BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo)
        self.LoanId = LoanId
        self.Type = Type
        self.AcctNo = AccountId


# input from user
m = input('Provide Bank Name: ')

n = input('Provide Bank Id: ')

i = input('Provide Bank Location: ')
d = input('Are you a customer(C) or a teller(T):\n').upper()
# if condition to test for customer or teller
if d == 'C':
    j = 1
    # while loop to allow only ten customer
    while j < 11:
        j += 1
        A, B, C, D = input('Customer Name:\n'), input('Your Address:\n'), \
            int(input('Phone Number')), input('Account Number:\n')
        Cus_1 = Customer(n, m, i, j, D, A, B, C)
        # While loop to allow use of different function by the same customer
        while True:
            E = int(input('Press: 1 for General inquiry , 2 for Depositing , 3 for withdrawing, 4 for Requesting,'
                          ' 5 for Loan Application, 6 Open Account, 7 Close Account, 8 Quit'))
            if E == 1:
                Cus_1.GeneralInquiry()
            elif E == 2:
                F = int(input('Enter amount to deposit \n'))
                Cus_1.DepositMoney(F)
            elif E == 3:
                G = int(input('Enter amount to withdraw\n'))
                Cus_1.WithdrawMoney(G)
            elif E == 4:
                Cus_1.RequestCard()
            elif E == 5:
                H = int(input('Enter amount of loan you need:\n'))
                Cus_1.ApplyForLoan(H)
            elif E == 6:
                Cus_1.OpenAccount()
            elif E == 7:
                Cus_1.CloseAccount()
            elif E == 8:
                break
# switch to the teller side for function

elif d == 'T':
    b, c, d, e, f, g = input('TellerID:\n'), input('Provide Customer Name:\n'),\
                        input('Enter your Address:\n'), int(input('Enter your phone Number')),\
                        input('Enter Your Account Number:\n'), input('Enter CustomerId:')
    Teller = Teller(b, n, m, i, g, f, c, d, e)

# While loop to allow the functionality of the Teller
    while True:
        h = int(input('Enter: 1 for General inquiry\n , 2 for Depositing\n , 3 for withdrawing\n, 4 for Requesting\n,'
                ' 5 for Loan Application\n, 6 Open Account\n, 7 Close Account\n, 8 Quit\n, 9 Provide Info\n, '
                             '10  Work on loan Request\n, 11 IssueCard\n,'))
        if h == 1:
                Teller.GeneralInquiry()
        elif h == 2:
                F = int(input('Please enter the amount you want to deposit in figure\n'))
                Teller.DepositMoney(F)
        elif h == 3:
                G = int(input('Please enter the amount you want to withdraw\n'))
                Teller.WithdrawMoney(G)
        elif h == 4:
                Teller.RequestCard()
        elif h == 5:
                H = int(input('Enter the amount of loan you need in figures\n'))
                Teller.ApplyForLoan(H)
        elif h == 6:
                Teller.OpenAccount()
        elif h == 7:
                Teller.CloseAccount()
        elif h == 8:
                break
        elif h == 9:
                Teller.ProvideInfo()
        elif h == 10:
                U = int(input('Please Enter loanId for the  Customer:'))
                t = input('Enter loan type requested by Customer:')
                Teller.LoanRequest(U, t)
        elif h == 11:
                Teller.IssueCard()





