print("Temperature Tracker (type 'quit' to stop)")

temperature_list = []

temperature = input("Enter temperature or 'quit': ")

while temperature != "quit":
    temp = float(temperature)
    temperature_list.append(temp)

    temperature = input("Enter temperature or 'quit': ")

# After loop (when user types quit)
if len(temperature_list) > 0:
    total = 0

    for t in temperature_list:
        total += t

    average = total / len(temperature_list)

    highest = temperature_list[0]
    lowest = temperature_list[0]

    for t in temperature_list:
        if t > highest:
            highest = t
        if t < lowest:
            lowest = t

    print("\nResults:")
    print("Temperatures:", temperature_list)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Average:", average)

else:
    print("No temperatures entered.")            
