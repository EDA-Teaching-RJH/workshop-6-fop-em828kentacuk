
mission_log = [
    {"Site": "Crater A ", "Radiation": "Low", "Water": False},
    {"Site": "Dune B, ", "Radiation": "High", "Water": True},
]

rover_status = [
    {"Battery": "100"},
    {"Heater": "Off"},
    {"Camera": "Standby"},
    {"Speed": "0"},

]



print("Battery status: " + rover_status[0]["Battery"])

start_moving = input("Start moving? (y/n): ")

if start_moving == "y":

    rover_status [1]["Heater"] = "On"
    rover_status [3]["Speed"] = "5"
    rover_status [0]["Battery"] = "85"


print("Battery status: " + rover_status[0]["Battery"])
print("Heater status: " + rover_status[1]["Heater"])
print("Speed: " + rover_status[3]["Speed"])
print("Camera status: " + rover_status[2]["Camera"])


if start_moving == "n":
    print("Rover remains stationary.")

analyse_mission = input("Analyse mission log? (y/n): ")
if analyse_mission == "y":
    for entry in mission_log:
        print("Site: " + entry["Site"] + "Radiation: " + entry["Radiation"])
        print("-----")


