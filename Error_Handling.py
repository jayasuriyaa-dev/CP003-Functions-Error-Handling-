try:
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))
    
    def safe_divide(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "cannot divide by Zero"
        except TypeError:
            return "Please enter numbers only"
        except ValueError:
            return "please enter as numerics"
    print("Result:",safe_divide(x, y))
  
except ValueError:
    print("Invalid Input! please enter as numerics.")
