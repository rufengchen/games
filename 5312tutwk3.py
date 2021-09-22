# 5312 WK3
# WK3 1.1
# For loop with range function
num_1 = int(input("Enter a number from 1 through 20: "))
for i in range(1,num_1+1):
    print('*'*i)

# WK3 1.2
# For loop with range function(nested loop)
# from **** to*
num_2 = int(input("Enter a number from 1 through 20: "))
for x in range(1,max(round((num_2+1)/num_2/2),2)):
    for y in range(num_2-1,0,-1):
        new='*'*y+' '*x
        print(new)

# WK3 1.2
# For loop with range function
# from **** to*
# do no need nested loop
num_21 = int(input("Enter a number from 1 through 20: "))
for i in range(num_21-1,0,-1):
    print('*'*i)


# 1.3 loop with item in a list
months = ["January","February","March","April","May","June","July",
         "August","September","October","Novermber","December"]
new_list_1_3 = []
# create a loop to make a new list contain three-letter abbreviation
for m in months:
    new_list_1_3.append(m[0:3])
print(new_list_1_3)


# WK3 1.4 Create a Menu
print("Enter a number from the menu to obtain a fact:")
print("1: Where is the heart of a shrimp located?")
print("2: What is the only animal that can't jump?")
print("3: For an ostrich, is the eye bigger than its brain?")
print("4: What is the English word with the most defintions?")
print("5: Quit")


while True:
    selection = eval(input("Make a selection from the menu: "))
    if selection == 1:
        print("Head")
    elif selection == 2:
        print("Elephant")
    elif selection == 3:
        print("Ostrich's eye is bigger than it's brain")
    elif selection == 4:
        print("Set")
    else:
        print("Thank you for using our quiz! Bye")
        break
