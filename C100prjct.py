class ATM(object):
    def __init__(self,cardNo,pinNo):
        self.cardNo=cardNo
        self.pinNo=pinNo
 
    def CashWithdrawn(self,object):
        print("Cash Withdrawn",object)

    def BalanceEnquiry(self,object):
        print("Balance is ",object)

Pranav=ATM("11008899","5234")
print(Pranav.cardNo)
print(Pranav.pinNo)
Pranav.CashWithdrawn(500)
Pranav.BalanceEnquiry(500)
