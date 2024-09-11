# Task 1: Start
temp_in_f = float(input("Enter the temperature in Fahrenheit: "))

# Task 2: Temperature Conversion
def fahrenheit_to_celsius(fahrenheit):
    try:
        temp_in_c = round((fahrenheit - 32) * 5/9, 1)
        print(f"{temp_in_f} degrees Fahrenheit is {temp_in_c} degrees Celsius.")
    except ValueError:
        print("Invalid input. Make sure to enter a number.")

# Task 3: User Experience - See above

# Task 4: Finally
    finally:
        print("Thank you for using the Weather Forecast Application!")
        
fahrenheit_to_celsius(temp_in_f)