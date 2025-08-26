#   Name: Landin Schenkel
#   Assignment: 1
#   Program Name: BMI processor
#   Date: 08/25/25

#   Get Function
def main():
    weight = float(input("Input your weight: "))
    height = float(input("Input your height: "))
    BMI = (weight * 703) / (height) ** 2
    if (BMI >= 18.5 and BMI <=25):
        print("Your BMI is optimal")
    elif (BMI < 18.5):
        print("You are Underweight")
    elif (BMI > 25):
        print("You are Overweight")

#   Call Function
main()
 