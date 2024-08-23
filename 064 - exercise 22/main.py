# check a number is prime or not 

def prime ():
    n = int(input("Enter a number : "))
    if( n==1):
        print("Number is not prime")
        return
    for i in range(2,n):
        if( n%i == 0 ):
            print("Number is not prime")
            return
    print("Number is prime")

prime()