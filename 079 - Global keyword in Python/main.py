# a=10

def dis():
    # print('dis start',a)
    a = 123
    # a=a+1
    # global a
    # a = a+1
    print("dis",a)
    
    def show():
        global a
        a=23
        print("show",a)
    
    print("dis show",a)
    show()
    print("show dis",a)

# print("main",a)
dis()
print("main",a)