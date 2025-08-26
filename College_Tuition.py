#   Name: Landin Schenkel
#   Assignment: 1
#   Program Name: Loop
#   Date: 08/25/25

tuition = 8000.0
increase_rate = .03

print("The increased rate for the next 5 years:")

for year in range(1, 6):
    tuition += tuition * increase_rate
    print("Year: ", year, " Tuition: $%.2f" % tuition)