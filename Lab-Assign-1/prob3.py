# Sample data
temperature_readings = [30, 32, 29, 31, 28, 27, 33]

total_temperature = 0
# Computes for total temperature for the week
for temperature in temperature_readings :
  total_temperature += temperature

# Computes for average temperature for the week
average_temperature = round(total_temperature / len(temperature_readings), 2)

# Display both the total and average temperature
print("🌤️ Weekly Weather Report")
print("-" * 30)
print(f"🌡️ Total temperature: {total_temperature}°C")
print(f"📊 Average temperature: {average_temperature}°C")
