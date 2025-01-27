print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def divisors(num): 
    divisor_list = []
    for i in range(2, num):
        if num % i == 0:
            divisor_list.append(i)
    return divisor_list

print(divisors(18))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def factors(num, factor):
    factors = divisors(factor)
    if num in factors:
        return True
    else:
        return False

print(factors(18, 2))
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def find_position(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    return alphabet.index(letter.lower())
print(find_position('z'))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def create_id(first_name):
    indexes=[]
    for letter in first_name:
        index = str(find_position(letter))
        indexes.append(index)
    id = ''.join(indexes)
    return id

print(create_id('alex'))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def create_password(first_name):
    id = list(create_id(first_name))
    sum = 0
    for num in id:
        sum += int(num)
    return int(''.join(id)) - sum

print(create_password('alex'))
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

def is_prime(num):
    if num == 0 or num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
print(is_prime(3))


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def is_prime_with_error(num):
    try:
        num = int(num)
        is_prime(num)
    except:
        print('Please input a number')
print(is_prime_with_error('four'))
# -------------------------------------------------------------------------------------- #






