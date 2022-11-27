air_temperature = float(input("Please enter the air temperature in degree Celsius: "))
wind_speed = float(input("Please enter the wind speed in km/h: "))

wind_chill = 13.12 + 0.6215 * air_temperature - 11.37 * wind_speed ** 0.16 + 0.3965 * air_temperature * wind_speed ** 0.16

print("The wind chill is", round(wind_chill))