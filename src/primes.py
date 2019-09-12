import math
CONSTindent = 200
class Primes:
    def __init__(self,size = 1400):
        self.size = size
        self.primes = self.seive(size)
    
    def __len__(self):
        return len(self.primes)
    
    def __getitem__(self,idx):
        return self.primes[idx]

    def __repr__(self):
        return str(self.primes)
    
    def seive(self,size):
        # print(size)
        ledger = [1 for i in range(size)]
        ledger[0] = 0
        ledger[1] = 0
        primes    = []
        i = 2
        while i < size:
            if ledger[i]:
                primes.append(i)
                j = i*2
                while j < size:
                    ledger[j] = 0
                    j+=i
            i+=1
        return primes
    

x = Primes()

