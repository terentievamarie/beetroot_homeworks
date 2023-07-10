def calculate_2(a,b):
    try:
        return int(a)**2/int(b)
    except ZeroDivisionError:
        raise ZeroDivisionError("Oops!You can't divide by zero.")
    except ValueError:
        print("You must enter numbers!Try again")

print(calculate_2(input("Please,enter first number: "),input("Please,enter second number: ")))
