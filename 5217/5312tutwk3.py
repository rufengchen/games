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
# Wk3 1.6
# reading txt files
# 1.6.1)  display the last row in the given file
faculty1 = open('faculty.txt','r') # 'r' means for reading
for row_1 in faculty:
    pass
print(row_1.rstrip())
faculty1.close() # for files we need to open the file and close the file
# pass: you want loop to cycle through the sequence and do nothing

# Wk3 1.6.2)
# find all the emails in the file and save to a list email_list
# print out all the emails
faculty2 = open('faculty.txt','r') # 'r' means for reading
for row in faculty:
    email_list = []
    if '@' in row:
        new_row = row.lstrip('Email: ').rstrip('\n') # remove 'Email:' on the left and '\n' on the right side
        email_list.append(new_row)  # add the row into the email_list
        print(email_list)
faculty2.close()


# Wk 3 1.7
# Reading csv files
# 1.7.1)
fruit1 = open('fruit_list.csv','r')
new_list = []
for item in fruit1:
    if 'grapes' in item:
        new_list.append(item.rstrip('\n')) # add the infor to the new list and remove '\n'
print(new_list)
fruit1.close()
