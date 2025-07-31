def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return celsius_to_fahrenheit(value)
        elif to_unit == "kelvin":
            return celsius_to_kelvin(value)
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return fahrenheit_to_celsius(value)
        elif to_unit == "kelvin":
            return fahrenheit_to_kelvin(value)
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return kelvin_to_celsius(value)
        elif to_unit == "fahrenheit":
            return kelvin_to_fahrenheit(value)

    raise ValueError("Invalid temperature units.")

# Main driver
def main():
    print("Temperature Converter: Celsius ↔ Fahrenheit ↔ Kelvin")
    print("-----------------------------------------------------")

    while True:
        try:
            value = float(input("Enter temperature value: "))
            from_unit = input("Enter current unit (Celsius, Fahrenheit, Kelvin): ").strip().lower()
            to_unit = input("Enter unit to convert to (Celsius, Fahrenheit, Kelvin): ").strip().lower()

            result = convert_temperature(value, from_unit, to_unit)
            print(f"\n{value} {from_unit.capitalize()} = {result:.2f} {to_unit.capitalize()}\n")

        except ValueError as e:
            print(f"Error: {e}")

        again = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the Temperature Converter!")
            break

if __name__ == "__main__":
    main()
