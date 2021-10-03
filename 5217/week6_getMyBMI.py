# Exercise 6: write modules
#import BMI

#path ='/Users/chenrufeng/OneDrive - City University of Hong Kong/IS5312_python/wk5/wk5q6.py'
# a) create a folder named"bmi", which works as a package including two modules:
from bmi import week6_getBodyInfo, week6_calculateBMI
def main():
    kilograms = week6_getBodyInfo.getKgWeight()
    meters = week6_getBodyInfo.getMHeight()
    bmi = week6_calculateBMI.getBMI(kilograms,meters)
    return(week6_calculateBMI.BMIcategory(bmi))
main()

print(main())
