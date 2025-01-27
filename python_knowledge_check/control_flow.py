print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
loop_control = 0
while loop_control < 5:
    print(x[loop_control])
    loop_control += 1

print("\nQ1b\n")


# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for num in x:
    if num % 2 == 0:
        print(num)



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
loop_control = 0
while loop_control < 5:
    if x[loop_control] % 2 == 0:
        print(x[loop_control])
    loop_control += 1

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
first_letter = []
for name in names:
    first_letter.append(name[0])
print(first_letter)


print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
space_index = []
for name in names:
    space = name.index(' ')
    space_index.append(space)
print(space_index)

print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
initials = []

for name in names:
    names_split = name.split(' ')
    initials.append(names_split[0][0])
    initials.append(names_split[1][0])

print(initials)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
no_duplicates = []
for item in list_of_lists:
    if len(item) == len(set(item)):
        no_duplicates.append(item)
print(no_duplicates)
# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
# user_input = 0

# while user_input < 101:
#     user_input = int(input('Please input a number greater than 100: '))
#     print(user_input)

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
user_input = 0

while user_input < 100:
    user_input = int(input('Please input a number greater than 100: '))
    if user_input == 0 or user_input == 1:
        print('not prime')
    elif user_input > 1:
        for i in range(2, user_input):
            if user_input % i == 0:
                print('not prime')
                break
        print('prime')
        break
    print(user_input)




