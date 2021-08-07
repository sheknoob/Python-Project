import math

print("----------Welcome---------- \n")

print(" 1. Addition \n 2. Substraction \n 3. Multiplication \n 4. Division [first/second] \n 5. Square \n 6. Root \n")

def fun1():
    print("___________________________________________________________________________________________________ \n")
    x=int(input(("Which arithmetic operation you want to do [choose the number assigned to it] : ")))
    L=[1,2,3,4,5,6,]
    if x not in L:
        print("Enter correct value")
    else:
        print()

    if x==1 or x==2 or x==3 or x==4 :
        num1=float(input("Enter first number : "))
        num2=float(input("Enter second number : "))
        if x==1:
            sum1=num1+num2
            print("Sum of the two numbers is : ",sum1)
        elif x==2:
            diff=num1-num2
            print("Difference of the two numbers is : ",diff)
        elif x==3:
            pdt=num1*num2
            print("Product of the two numbers is : ",pdt)
        elif x==4:
            div=num1/num2
            print("Quotient is ",div)
        '''else:
            print("Enter correct value")'''

    if x==5 or x==6:
        num1=float(input("Enter number : "))
        if x==5:
            sq=num1*num1
            print("Square of ",num1,"is ",sq)
        elif x==6:
            root=math.sqrt(num1)
            print("Root of ",num1,"is ",root)
        '''else:
            print("Enter the correct value")'''
    '''else:
        print("Enter the correct value")'''
    print("\n")
    z=str(input("Do you wish to continue ? [y/n] : "))
    if z=='y':
        fun1()
    else:
        quit()        
    
fun1()


