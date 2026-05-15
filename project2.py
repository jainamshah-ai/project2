while True:
    print("\nwelcome to the pattern genertor and analyzer")
    print("\nselect an option")
    print("1. generate a pattern")
    print("2. analyze a range of numbers")
    print("3. exits")
    choice=int(input("enter your choice:"))

    if choice==1:
        rows=int(input("enter the number of rows in the pattern"))
        print("\npatterns:")
        for i in range(1,rows + 1):
            print("*"*i)
    
    elif choice==2:
        start=int(input("enter the starting of the range"))
        end=int(input("enter the ending of the range"))
        total=0
        for num in range(start,end +1):
            if num % 2 == 0:
                print(f"the number {num} is even")
            else:
                print(f"the number {num} is odd")
            total +=num
        print(f"sum of all total from {start} to {end} is {total}")   
    elif choice==3:
        print("exiting the programe,goodby")
        break
    else:
        print("invalid choice! please select again")