def calc(a1,a2,a3):
    add=a1+a2+a3
    sub=a1-a2
    mul=a1*a2
    print(f"value of a={a1},b={a2} & c={a3}")
    print(f"respons from calc --> add= {add}, sub ={sub} & Mul= {mul}")
    return add,sub,mul

def table(i):
    if i<6:        
        print(f"table of {i}")
        for x in range(1,11):
            print(f"{i} * {x} = {i*x}")
            t=i*x
        return t
    else:
        print(f"table of {i} not required")
    

def compare(a1,a2,a3):
    if (a1 > a2) & (a1 > a3):
        print(f"{a1} is greatest")
    elif (a2>a1) & (a2>a3):
        print(f"{a2} is greatest")
    elif (a3>a1) & (a3>a2):
        print(f"{a3} is greatest")
    else:
        print(f"'number are {a1}, {a2} & {a3} but observed some error'")
    return a1,a2,a3



