# Exercise 1: list sorting
# create one state a line and only contain the first 13 states
statefile = open("States.txt","r") # you get Str
statesstr = statefile.read() # read all the content
# Use split turn the Str into List, create a list of states using split()
statelist = statesstr.split('\n') #\n mean the seperator
# sort the 13 states in alphabetical order, extract the first 13 states
new_list = statelist[0:13]
new_list.sort()
print(new_list)
# display the 13 states one in one line
for i in range (0,len(new_list)):
    print(new_list[i])
statefile.close()


# Exercise 1: list sorting (another version)
# create one state a line and only contain the first 13 states
statefile1 = open("States.txt","r") # you get Str
statelist1 =[line for line in statefile1]# read lines, list comprehension
statelist1 = statelist1[0:13]
statelist1.sort()
for i in range(0,len(statelist1)):
    statelist1[i].replace('\n','')
    print(statelist1[i])
statefile1.close()


# Exercise 2: list comprehension and sorting with lambda function
names = ['Yuqi Lan','Marilyn Leung','Chenyu Zhang','Wing Sze Wong']
setLN =set()
for name in names:
    setLN.add(name.split()[-1])
print(setLN)


# Exercise 2: list comprehension and sorting with lambda function
# 2.1 use list comprehesion
names1 = ['Yuqi Lan','Marilyn Leung','Chenyu Zhang','Wing Sze Wong']
setLN1 = [lname1.split()[-1] for lname1 in names1]
print(setLN1)


# Exercise 2: list comprehension and sorting with lambda function
# 2.2 use lambda sort the name by last name
names2 = ['Yuqi Lan','Marilyn Leung','Chenyu Zhang','Wing Sze Wong']
setLN2 = [lname.split()[-1] for lname in names2]
names2.sort(key=lambda x: x.split()[-1])
print(names2)

# Another method:
def y(x):
    return x.split()[-1]
names3 = ['Yuqi Lan','Marilyn Leung','Chenyu Zhang','Wing Sze Wong']
names3.sort(key=y)# the key is the function name(no need parameters)
print(names3)