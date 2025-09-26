import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def sqrt(a):
    if a < 0:
        return "Error: Negative number"
    return math.sqrt(a)

def pounds_to_kg(pounds):
    return pounds * 0.453592

def kg_to_pounds(kg):
    return kg / 0.453592

def cm_to_m(cm):
    return cm / 100

def m_to_cm(m):
    return m * 100

def inch_to_feet(inch):
    return inch / 12

def feet_to_inch(feet):
    return feet * 12

def main():
    print("Complex Calculator")
    print("Type 'o', 'O', or 'OP' for Operations (add, subtract, multiply, divide, sqrt)")
    print("Type 'c', 'C', or 'con' for Conversions (pounds_to_kg, kg_to_pounds, cm_to_m, m_to_cm, inch_to_feet, feet_to_inch)")
    mode = input("Operation/Conversion mode: ").strip().lower()

    if mode in ["o", "op"]:
        op = input("Select operation (add, subtract, multiply, divide, sqrt): ").strip().lower()
        if op in ["add", "subtract", "multiply", "divide"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if op == "add":
                print("Result:", add(a, b))
            elif op == "subtract":
                print("Result:", subtract(a, b))
            elif op == "multiply":
                print("Result:", multiply(a, b))
            elif op == "divide":
                print("Result:", divide(a, b))
        elif op == "sqrt":
            a = float(input("Enter number: "))
            print("Result:", sqrt(a))
        else:
            print("Invalid operation.")
    elif mode in ["c", "con"]:
        conv = input("Select conversion (pounds_to_kg, kg_to_pounds, cm_to_m, m_to_cm, inch_to_feet, feet_to_inch): ").strip().lower()
        if conv == "pounds_to_kg":
            pounds = float(input("Enter pounds: "))
            print("Result:", pounds_to_kg(pounds), "kg")
        elif conv == "kg_to_pounds":
            kg = float(input("Enter kilograms: "))
            print("Result:", kg_to_pounds(kg), "pounds")
        elif conv == "cm_to_m":
            cm = float(input("Enter centimeters: "))
            print("Result:", cm_to_m(cm), "meters")
        elif conv == "m_to_cm":
            m = float(input("Enter meters: "))
            print("Result:", m_to_cm(m), "centimeters")
        elif conv == "inch_to_feet":
            inch = float(input("Enter inches: "))
            print("Result:", inch_to_feet(inch), "feet")
        elif conv == "feet_to_inch":
            feet = float(input("Enter feet: "))
            print("Result:", feet_to_inch(feet), "inches")
        else:
            print("Invalid conversion.")
    else:
        print("Invalid mode.")

if __name__ == "__main__":
    main()