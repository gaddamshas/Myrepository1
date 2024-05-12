class Calc:
    CNT = 0
    def __init__(self,a,b):
        self.n1 = a
        self.n2 = b
        Calc.CNT += 1

    def addition(self):
        return self.n1 + self.n2

#a = Calc(10,12)
#res = a.addition()
#print(a.addition())


class NewCalc(Calc):

    def substraction(self):
        return self.n2 - self.n1


a1 = NewCalc(45,86)
print(f'Addition of {a1.n1} and {a1.n2} = {a1.addition()}')
print(f'Substration of {a1.n1} and {a1.n2} = {a1.substraction()}')
print('\n')
a2 = NewCalc(23,34)
print(f'Addition of {a2.n1} and {a2.n2} = {a2.addition()}')
print(f'Substration of {a2.n2} and {a2.n1} = {a2.substraction()}')
#print(f'Number of objects crated = {Calc.CNT}')
print('\n')
a3 = NewCalc(43,57)
print(f'Addition of {a3.n1} and {a3.n2} = {a3.addition()}')
print(f'Substration of {a3.n1} and {a3.n2} = {a3.substraction()}')
print(f'\nNumber of objects crated = {Calc.CNT}')
