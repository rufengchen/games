class week6_getBodyInfo():
    def getKgWeight():
        pounds = float(input('Please enter your weight in pounds: '))
        kg = pounds * 0.453592
        return round(kg, 2)

    def getMHeight():
        feet = int(input("Please enter your height in feet: "))
        inches = float(input("Please enter your height in inches: "))
        heightInches = feet * 12 + inches
        meters = heightInches * 0.0254
        return round(meters, 2)
class week6_calculateBMI():
    def getBMI(kilograms, meters):
        bmi = kilograms / (meters ** 2)
        return round(bmi, 2)

    def BMIcategory(bmi):
        if bmi < 18.3:
            print('You are underweight')
        elif bmi < 25 and bmi >= 18.3:
            print('You are normal weight')
        elif bmi < 30 and bmi >= 25:
            print('You are overweight')
        else:
            print('You should see a doctor')
