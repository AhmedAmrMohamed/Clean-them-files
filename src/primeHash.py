from primes import Primes
class PrimeHash:
    def __init__(self):
        self.primes = Primes().primes
        self.table   = self.buildtable()

    def buildtable(self):
        table = {}
        start = ord('a')
        end   = ord('z')
        prptr = 0
        while start < end:
            table[chr(start)] = self.primes[prptr]
            start+=1
            prptr+=1
        return table
    
    def hash(self,word):
        res = 1
        for i in word:
            if i.isalpha():
                c = i.lower()
                res *= self.table[c]
        return res


x = PrimeHash()
a = x.hash('ahmed')
b = x.hash('demha')
