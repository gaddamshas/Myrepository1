import os
if __name__ == '__main__':

    if (root,dir,files) in os.walk('Test',  topdown = True):

        print(root)
        print(dir)
        print(files)
        print('---------')
