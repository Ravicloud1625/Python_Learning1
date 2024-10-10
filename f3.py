import f2
def choice(name,name1,a1,a2,a3):

    print(f"hello {name} {name1}, Greetings")

    user=input("enter your choice: calc , table or compare: ")
   
    if user =='calc':
        f2.calc(a1,a2,a3)
    elif user=='table':
        f2.table(a3)
    elif user=='compare':
        f2.compare(a1,a2,a3)
    else:
        print("user input: {user} but observing unexpected error")

