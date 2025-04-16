def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        return result
    except ValueError:
        print("It's an Error. Please enter only integers.")
    except ZeroDivisionError:
        print("Error. Devision by Zero is not possible. ")
division_result = divide_numbers()
if division_result is not None:
    print(f"Division result is: {division_result}")
