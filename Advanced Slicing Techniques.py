#Task 1:


temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temperatures = temperatures[7:14]
print("Temperatures for the second week:", second_week_temperatures)




#Task 2:


temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
above_100_temperatures = [hot for hot in temperatures if hot > 100]
print("Temperatures above 100:", above_100_temperatures)




#Task 3:


temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
temperatures.reverse()
extracted_temperatures = temperatures[4:10]
print("Temperatures between the 5th and 10th day of the reversed list:", extracted_temperatures)
