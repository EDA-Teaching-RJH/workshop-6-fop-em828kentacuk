

status = [
    {"Power": "100"},
    {"Samples": "0"},
]
inventory = []
while True:
    print("Menu")
    print("1. Collect Sample")
    print("2. Report Status")
    print("3. Emergency Stop")
    choice = int(input("Select Option: "))
    if choice == 1:
        new_sample = input("Enter sample name: ")
        inventory.append(new_sample)
        status[0]["Power"] = str(int(status[0]["Power"]) - 10)
        status[1]["Samples"] = str(int(status[1]["Samples"]) + 1)

    elif choice == 2:
        print("Power: " + status[0]["Power"] + "%")
        print("Samples Collected: " + status[1]["Samples"])

    elif choice == 3:
        print("Emergency Stop Activated. Shutting down.")
    
    else:  print("Invalid option. Please select 1, 2, or 3.")
    break
            
