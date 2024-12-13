# Try, Except - look for documentation for all kinds of exceptions, Finally = always executes
# Exception will catch all exception, but its bad practice, do it as a last resort

try:
    number = int(input("Enter a number:"))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")