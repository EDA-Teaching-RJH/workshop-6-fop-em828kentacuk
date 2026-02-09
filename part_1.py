sample_types = ["Basalt", "Silica", "Iron" ,"Dust" ]
new_sample = []

sample_bay = [ 
    {"sample" : "Basalt"},
    {"sample" : "Silica"},
    {"sample" : "Iron"},
    {"sample" : "Dust"}
]

print("select option:")
print("1: View Bay Contents")
print("2: Transmit Sample")
print("3: Add new sample to bay")
print("4: Expel Dust")
option = int(input("Select option: "))

def main():
    if option == 1:
        print(sample_types[0])
        print(sample_types[3])
        print(len(sample_types))

    elif option == 2:
        for sample in sample_types:
            print("Transmitting sample: " + sample)
    elif option == 3:
        while len(new_sample) < 3:

            new_sample1 = input("Enter 1st new sample type: ")
            new_sample2 = input("Enter 2nd new sample type: ")
            new_sample3 = input("Enter 3rd new sample type: ")
            new_sample.append(new_sample1)
            new_sample.append(new_sample2)
            new_sample.append(new_sample3)
            print("New samples added to bay: " + str(new_sample))
    elif option == 4:
        if "Dust" in sample_types:
            sample_types.remove("Dust")
            print("Dust expelled from bay.")
        else:
            print("No dust to expel.")

  
main() 