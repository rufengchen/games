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