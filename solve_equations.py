def linear_equation(a,b):
    a=-(b)
    print("only one possible solution",a)

#i have used this def in all others after this
def quadratic_equation(a,b,c):
    d = b**2-4*a*c # discriminant

    if d < 0:
        print ("This equation has no real solution, QUADRATIC ERROR")
    elif d == 0:
        xx = (-b+((b**2-4*a*c)**0.5))/2*a
        print ("This equation has one solutions: ",xx)
    else:
        x1 = (-b+(((b**2)-(4*(a*c)))**0.5))/(2*a)
        x2 = (-b-(((b**2)-(4*(a*c)))**0.5))/(2*a)
        #print ("The equation ",a,"x2 + ",b,"x + ",c," has two solutions: ", x1, "and the other solution is" , x2)
        print("solution: ",x1)
        print("solution: ",x2)

#this is to solve the cubic equation, it simply reduces it to a quadratic equation 
def cubic_equation(a,b,c,d):
    i=-1000.0
    while (a*i*i*i)+(b*i*i)+(c*i)+(d)!=0 and i<10000:
        #print(i)
        i+=0.5
    else:
        if i>=10000:
            print("NO RESULT, CUBIC ERROR")
        else:
            root1=i
            print("solution: ",root1)
            expected_a=a
            expected_b=(a*root1)+b
            expected_c=(expected_b*root1)+c
            expected_d=(expected_c*root1)+d
            if expected_d!=0:
                print("root verification failed")
            else:
                #print("root verification succedded")
                quadratic_equation(expected_a,expected_b,expected_c)


#I have absolutely no idea about bi-quadratic equations, this is hit & trial
def biquadratic_equation(a,b,c,d,e):
    i=-1000.0
    while (a*i*i*i*i)+(b*i*i*i)+(c*i*i)+(d*i)+(e)!=0 and i<10000:
        #print(i)
        i+=0.5
    else:
        if i>=10000:
            print("NO RESULT, BIQUADRATIC ERROR")
        else:
            root1=i
            print("solution: ",root1)
            expected_a=a
            expected_b=(a*root1)+b
            expected_c=(expected_b*root1)+c
            expected_d=(expected_c*root1)+d
            expected_e=(expected_d*root1)+e
            if expected_e!=0:
                print("root verification failed")
            else:
                #print("root verification succedded")
                cubic_equation(expected_a,expected_b,expected_c,expected_d)
    
            
        

#this will the the input for coefficients, "0" to be entered where nothing is given
print("be sure type in zeros when required")
x=input("Enter space seperated coefficients: ")
list=list(map(int,x.split())) #the list tells that it is a list, the map i donno, the x tells what to split the empty () will split according to space entered
#print(list)

if len(list)==1:
    print("not acceptable, the power of variable is 0")
elif len(list)==2:
    print("this is a linear equation in one variable")
    l=int(list[0])
    m=int(list[1])
    linear_equation(l,m)
elif len(list)==3:
    print("this is a Quadratic equation in one varibale")
    l=int(list[0])
    m=int(list[1])
    n=int(list[2])
    quadratic_equation(l,m,n)
elif len(list)==4:
    print("this is a Cubic equation in one variable")
    print("Equation is of the form ax3 + bx2 + cx + d")
    l=int(list[0])
    m=int(list[1])
    n=int(list[2])
    o=int(list[3])
    cubic_equation(l,m,n,o)
elif len(list)==5:
    print("This is BiQuadratic Equation in one variable")
    l=int(list[0])
    m=int(list[1])
    n=int(list[2])
    o=int(list[3])
    p=int(list[4])
    biquadratic_equation(l,m,n,o,p)

else:
    print("not acceptable, the power of variable exceeds 5")


