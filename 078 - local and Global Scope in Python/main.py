# global variable
a = 10

def display():
    # local variable
    a = 15
    print("fun",a)

    def show():
        print("show",a)
    
    show()

display()
print("main",a)


a,b = 5,6

if( a<b):
    c = a+b

print("c",c)

