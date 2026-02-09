
inventory = []

status = [
    {"Power": "100"},
    {"Samples": "0"},

]


start_mission = input("Start mission? (y/n): ")


travel_log = []

if start_mission == "y":
    while True:
        try:
            angle = int(input("Enter angle (0-90): "))
        except ValueError:
            print("Error: Corrupted Signal. Unable to retrieve angle.")
            continue
        if angle > 45:
            print("CRITICAL TILT! HALTING.")
        else:
            travel_log.append(angle)
            print("Path Stable - Continuing.")
            end_mission = input("End mission? (y/n): ")
            if end_mission == "y":
                print("Mission Ended. Travel Log: " + str(travel_log))
                break
        
    

