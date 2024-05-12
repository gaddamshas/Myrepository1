class Color:

    def __init__(self):

        self.name = 'Green'
        self.subcolor = self.Light_green()

    def display(self):
        print('Name of main color:', self.name)


    class Light_green:
        def __init__(self):

            self.name = 'Light Green'
            self.code = '024avc'

        def show(self):

            print('Name:', self.name)
            print('Code', self.code)

# Color class object
oc = Color()

#method calling
oc.display()

#Light_green
#inner clss
g = oc.subcolor

#inner class method calling
g.show()

