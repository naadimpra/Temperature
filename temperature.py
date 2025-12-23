def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Converts Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Converts Kelvin to Celsius."""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Converts Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    """Converts Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("\n--- Professional Temperature Converter ---")
    print("1. Celsius to Fahrenheit/Kelvin")
    print("2. Fahrenheit to Celsius/Kelvin")
    print("3. Kelvin to Celsius/Fahrenheit")
    
    choice = input("Select an option (1-3): ")
    
    try:
        val = float(input("Enter the temperature value: "))
        if choice == '1':
            print(f"{val}°C = {celsius_to_fahrenheit(val)}°F and {celsius_to_kelvin(val)}K")
        elif choice == '2':
            print(f"{val}°F = {fahrenheit_to_celsius(val)}°C and {fahrenheit_to_kelvin(val)}K")
        elif choice == '3':
            print(f"{val}K = {kelvin_to_celsius(val)}°C and {kelvin_to_fahrenheit(val)}°F")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Error: Please enter a numeric value.")

if __name__ == "__main__":
    main()