
def main():
    try:
        motor_speed = int(input("Enter motor speed (0-10): "))
        if 0 <= motor_speed <= 10:
            print(f"Motor speed set to {motor_speed}.")
    except ValueError:
        print("Error: Corrupted Signal. Maintaining current speed.")

    def get_coordinate():
        while True:
            try:
                x_coord = int(input("Enter X coordinate: "))
                if -100 > x_coord > 100:
                    print("Error: Corrupted Signal. Coordinate out of range.")
                    return None
            except ValueError:
                print("Error: Corrupted Signal. Unable to retrieve coordinate.")
                return None
            return x_coord
    get_coordinate()



main()        
    
