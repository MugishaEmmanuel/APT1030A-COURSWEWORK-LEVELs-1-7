print("Welcome to rainfall advisory! ")

rainfall = int(input("Enter the rainfall amount in mm: "))
temperature = int(input("Enter temperature in degree Celsius(°C): "))

if rainfall < 200:
    print("Irrigation Required")
else:
    if temperature > 30:
        print("Monitor Soil")
    else:
        print("Normal Conditions")