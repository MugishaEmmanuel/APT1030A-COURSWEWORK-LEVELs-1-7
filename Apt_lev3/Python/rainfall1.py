print("Welcome to rainfall advisory! ")

rainfall = int(input("Enter the rainfall amount in mm: "))
temperature = int(input("Enter temperature in degree Celsius(°C): "))

if rainfall < 200:
    print("Irrigation Required")
elif rainfall >= 200 and temperature > 30:
    print("Monitor Soil")
else:
    print("Normal Conditions")