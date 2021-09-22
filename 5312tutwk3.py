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