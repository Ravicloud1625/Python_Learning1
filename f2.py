def calc(a1,a2,a3):
    add=a1+a2+a3
    sub=a1-a2
    mul=a1*a2
    print(f"value of a={a1},b={a2} & c={a3}")
    print(f"respons from calc --> add= {add}, sub ={sub} & Mul= {mul}")
    return add,sub,mul

def table(a3):
    print(f"value of c={a3}")
    if a3<6:        
        print(f"table of {a3}")
        for x in range(1,11):
            print(f"{a3} * {x} = {a3*x}")
            t=a3*x
        return t
    else:
        print(f"table of {a3} not required")
    

def compare(a1,a2,a3):
    print(f"value of a={a1},b={a2} & c={a3}")
    if (a1 > a2) & (a1 > a3):
        print(f"{a1} is greatest")
    elif (a2>a1) & (a2>a3):
        print(f"{a2} is greatest")
    elif (a3>a1) & (a3>a2):
        print(f"{a3} is greatest")
    else:
        print(f"'number are {a1}, {a2} & {a3} but observed some error'")
    return a1,a2,a3



