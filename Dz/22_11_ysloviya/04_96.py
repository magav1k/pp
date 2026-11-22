a = float(input("введите a: "))
b = float(input("введите b: "))
c = float(input("введите c: "))
x_1=0
x_2=0
discr=0
if a==0 or b==0 or c==0:
    print("числа не должны быть равны 0")
else:
    discr = b**2 - 4*a*c 
    if discr>0:
        x_1 = (-b-(discr**0.5))/2*a
        x_2 = (-b+(discr**0.5))/2*a
        print(f"корень 1: {x_1}, корень 2: 1{x_2}")

    elif discr==0:
        x_1 = (-b+(discr**0.5))/2*a

        print(f"корень 1: {x_1}") 

    else: print("корней нет")    

