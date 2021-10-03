# model1: week6_getBodyInfo
def getKgWeight():
    pounds = float(input('Please enter your weight in pounds: '))
    kg = pounds * 0.453592
    return round(kg,2)
def getMHeight():
    feet = int(input("Please enter your height in feet: "))
    inches = float(input("Please enter your height in inches: "))
    heightInches = feet *12 + inches
    meters = heightInches *0.0254
    return round(meters,2)