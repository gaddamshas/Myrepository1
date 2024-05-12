class A:
                     #if we don't create constructor then python will implicitely
    a = 10          # inject default constructor-->'def __init__(self)'

    def show(self):

        print(self.a)

ob = A()
ob.show()
