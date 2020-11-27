def temp_calculator(temperature):
    celcius = (temperature-30) / 2
    return celcius

temperature = int(input("What fahrenheit temperature would you like to convert? "))
celcius = temp_calculator(temperature)

print("The celcius value of ",temperature, " is ", celcius)
