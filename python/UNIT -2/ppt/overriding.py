class Bank:
    def getTroi(self):
        return 10

class SBI(Bank):
    def getTroi(self):
        return 7

b1 = Bank()
b2 = SBI()

print('Bank rate of interest :',b1.getTroi())
print('SBI rate of interest :',b2.getTroi())