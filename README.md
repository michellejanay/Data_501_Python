# Python <a name="python-fundamentals"></a>
This is a brief tutorial on some basic Python Fundamentals. 

## Table of Contents
- [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Pycharm](#pycharm)
    - [Comments](#comments)
- [Data Types](#data-types)
    - [Numbers and Math Operators](#numbers-and-math-operators)
    - [String Basics](#string-basics)
    - [Boolean and Equality Operators](#boolean-and-equality-operators)
- [Variables](#variables)
- [More on Strings](#more-on-strings)
    - [Concatenation and Escape Characters](#concatenation-and-escape-characters)
    - [String Methods](#string-methods)
- [Control Flow](#control-flow)
- [Collections](#collections)
    - [Lists](#lists)
    - [Dictionaries](#dictionaries)
- [Loops](#loops)
    - [While Loops](#while-loops)
    - [For Loops](#for-loops)
- [Functions](#functions)

## Getting Started <a name="getting-started"></a>


### Installation <a name="installation"></a>
Head over to [Python.org/downloads](https://www.python.org/downloads/) to install the latest version of Python. The browser will automatically be able to tell which operating system you are on.<br>
Follow the installation steps. <br>
To check that it has successfully install, in your terminal type <br>
`python --version` <br>
and you should see the version of Python you installed<br>


### Pycharm <a name="pycharm"></a>
Pycharm is a Python Integrated Developement Environment (IDE) for Data Science and Web Development.<br>
To download head over to [Pycharm](https://www.jetbrains.com/pycharm/download/) and scroll to the bottom of the page to get the Community(free) version.<br>
Run the installation and open the application. Now you are ready to get started in writing Python!

### Comments <a name="comments"></a>
Commenting code is a great way to leave notes for yourself when starting your coding journey. The code editor will ignore everything after or within your comments<br> 
There are two ways to comment out code:

1. Inline comment - for a singular line uses the `#` symbol.<br>
`# This is a comment`

2. Block comment - for commenting out multiple lines of code in Python you use triple quotes<br>
``` 
"""
This is a multi-line comment
"""
```

### Print Statement
We will be using the print statement a lot in this tutorial. The print statement allows you to see the result/message you want to print. Test it out in Pycharm by running <br>

`print('hello world!')`

See the result in your terminal.<br>

*To run your code in Pycharm, press the play button in the top right corner, or right-click the file and select run file-name*

## Data Types <a name="data-types"></a>
Python has many built in data types. Three of the main ones are 
1. Numbers
    - Integers (whole numbers)
    - Floats (decimal numbers)
2. Strings (text)
3. Booleans (True/False)


### Numbers and Math Operators <a name="numbers-and-math-operatorss"></a>

 Syntax      | Description | Example |
| ----------- | ----------- | ----------- |
| +      | **Add** | 1 + 1 (2) |
| -   | **Subtract** | 6 - 1 (5) |
| *   | **Multiply** | 5 - 3 (15) |
| /   | **Divide** | 4 / 2 (2) |
| %   | **Modulo** - returns remainer | 5 % 2 (1) |

Test them out in Pycharm by running them inside a print statement in a Python file.<br><br>
**Example:**<br>

```
print(1 + 1)
# result is 2
```

#### Handy hint

Check the data type in Python by using the `type()` method:<br>

```
print(type(5))
# returns integer
```

### String Basics <a name="string-basics"></a>
Strings are pretty much anything that involve characters or text. Strings can use either double or single quotes: <br>

`print('hello world')`<br>
is the same as <br>
`print("hello world")`

It's important to note that Python, or any other programming languages, do not see words, sentances, or paragraphs. They see Unicode characters within single or double quotes

To find out more about Unicode click [here](https://home.unicode.org/).

#### Indexing in Strings
As a string is basically a list of characters, we can use indexing is a way to find a specific character or characters in our string. Indexes start at 0 and count upwards. We can also use negative values for indexing. We use squarebracket syntax for indexing<br><br>

**Examples:**
```
print('hello pycharm!'[0])
# returns h
```
```
print('hello pycharm!'[6])
# returns p
```
```
print('hello pycharm!'[-1])
# returns !
```

_Note: spaces are counted as characters in strings_

#### Finding the Length of a String
In Python, we use the in-built len function to find the number of characters in a string. It returns an integer<br><br>

**Example:**
```
print(len('hello world!'))
# returns 14
```

### Boolean and Equality Operators <a name="boolean-and-equality-operators"></a>
Booleans return a True/False value. <br><br>

**Equality Operators that return Boolean Values**
 Syntax      | Description | Example |
| ----------- | ----------- | ----------- |
| ==      | **Equal to** | 'one' == 'one' (True) |
| !=   | **Not Equal to** | 2 != 1 (True) |
| >   | **Greater than** | 3 > 5 (False) |
| <   | **Less than** | 4 < 2 (False) |
| >=   | **Greater than or Equal to** - returns remained | 5 <= 2 (True) |
| <=   | **Less than or Equal to** - returns remained | 5 >= 2 (False) |

Try them out in Pycharm using the terminal. What happens when you check the type string against an integer?<br>

We can also use the in-built bool function to check if a value is true or false.<br><br>

**Examples with integers**
```
print(bool(1))
# returns True
```
```
print(bool(0))
# returns False
```
```
print(bool(-1))
# returns True
```

**Examples with strings**
```
print(bool('hello'))
# returns True
```
```
print(bool(''))
# returns False
```

_Note: Anything other than 0 is considered True in Python_

## Variables <a name="variables"></a>
Variables are a resevered memory location that allow us to store data types and objects. They can have any name you like, but be sure to use meaningful names when naming variabls.<br><br>

**Example**
```
greeting = 'hello world!'
print(greeting)
# returns hello world!
```

Variables with multiple words use the snake case typing. This is a convention and can use other typing such as CamelCase. I would recommend following the Python style guide [here](https://peps.python.org/pep-0008/) for more details<br><br>

**Example**
```
hello_world_greeting = 'hello world!'
print(hello_world_greeting)
# returns hello world!
```

It's also important to not that variables are _mutable_ and can change<br><br>

**Example**
```
greeting = 'hello world!'
greeting = 'hello python!'
print(greeting)
# returns hello python!
```

## More on Strings <a name="more-on-strings"></a>


### Concatenation <a name="#concatenation-and-escape-characters"></a>

Concatenation is the process of joining strings together<br><br>
**Example**<br>
```
first_name = 'Jane'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
print(full_name)
# returns Jane Doe
```

You cannot add a string to an integer. Instead, you must use the in-built str function to convert an integer to a string. This is called casting <br><br>

**Example**<br>
```
first_name = 'Jane'
age = 30
person_age = first_name + ' is ' + str(age) + ' years old.'
print(person_age)
# returns Jane is 30 years old.
```

Another important thing to note about strings are nested quotes. You can use double and single quotes interchangeably for this, or you can use escape characters<br><br>

**Example**
```
statement = 'Someone says "Strings can be tricky"'
print(statement)
# returns Someone says "Strings can be tricky"
```
or
```
statement = "Someone says 'Strings can be tricky'"
print(statement)
# returns Someone says 'Strings can be tricky'
```
or with escape characters
```
statement = "Someone says \"Strings can be tricky\""
print(statement)
# returns Someone says "Strings can be tricky"
```

Another common way of formatting strings is to use the `f` key in Python. This way we can pass variables direction into our string using curly brackets. <br><br>
**Example**<br>
```
first_name = 'Jane'
print(f'hello {first_name}!')
# returns hello Jane!
```

### String Methods <a name="string-methods"></a>
String methods are a set of built in methods we can use to adapt or change areas of a string. To see a comprehensive list of string methods click [here](https://docs.python.org/3/library/stdtypes.html#string-methods).

To see a list in Pycharm, type a `.` after your string or saved string variable and a list of various methods should pop up. Explore these in Pycharm<br><br>

**Examples**
```
first_name = 'jane'
print(first_name.capitalize())
# returns Jane
```
```
first_name = 'jane'
print(first_name.upper())
# returns JANE
```
```
first_name = 'jane'
print(first_name.replace('j', 'J'))
# returns Jane
```

## Control Flow <a name="control-flow"></a>
Control flow is how we make decisions on our data, as coding is not just about writing code, it's about solving problems.<br>

One way of using control flow in Python is to use if/else blocks. <br>
The way this works is as follows<br>

```
if (condition):
    print('This is what happens when a condition is met')
```

We can also say what we want to happen when a condition is not met

```
if (condition):
    print('This is what happens when a condition is met')
else:
    print('This is what happens when the condition is not met')
```

In addition, we can add multiple conditions called else-if statements

```
if (condition):
    print('This is what happens if the first condition is met')
elif (condition):
    print('This is what happens if the second condition is met')
elif (condition):
    print('This is what happens if the third condition is met')
else:
    print('this is what happens when the condition is not met')
```

**The code will stop executing when it finds the first matching condition.**<br>

In a real-world example, lets say we want to solve a once common coding interview challenge. If a number is divisible by 3, we want to print 'Fizz', if a number is divisible by 5, we want to print 'Buzz', and if a number is divisible by both, we want to print 'FizzBuzz'. Let's see how we can do that below.<br>

```
num = 3

if num % 15 == 0:
    print('FizzBuzz')
elif num % 5 == 0:
    print('Buzz')
elif num % 3 == 0:
    print('Fizz')

# returns Fizz
```
and if we change `num` 
```
num = 10

if num % 15 == 0:
    print('FizzBuzz')
elif num % 5 == 0:
    print('Buzz')
elif num % 3 == 0:
    print('Fizz')

# returns Buzz
```
and if we change `num` again
```
num = 30

if num % 15 == 0:
    print('FizzBuzz')
elif num % 5 == 0:
    print('Buzz')
elif num % 3 == 0:
    print('Fizz')

# returns FizzBuzz
```

What happens when a number is not divisible by 3, 5, or 15? <br>
The code block will return nothing because none of the conditions are met. To fix this we can add an else statement<br>

```
num = 22

if num % 15 == 0:
    print('FizzBuzz')
elif num % 5 == 0:
    print('Buzz')
elif num % 3 == 0:
    print('Fizz')
else:
    print(f'{str(num)} is not divisible by 3, 5, or 15.')

# returns 22 is not divisible by 3, 5, or 15.
```


## Collections <a name="collections"></a>
Collections are built-in types that allow us to store larger amounts of data in a particular format. The two formats we are focusing on here are lists and dictionaries.

### Lists <a name="lists"></a>
Also know as Arrays in other coding languages do exactly what their name suggests. You can store any data type in a list. A list is wrapped in square brackets, seperated by commas and uses the same indexing as strings, starting at 0. <br><br>

**Example**
```
my_list = ['String', 1, 2.3, True, ['Another list']]
print(my_list[3])
# returns True
```


### Dictionaries <a name="dictionaries"></a>
Dictionaries, also know as HashMap or Maps, are based on **key** **value** pairs. In lists we use indexes, but in dictionaries we can give a key that will store our information. We seperate keys from values using a colon. Keys will often be string values of any name, and the values can be any data type. We use bracket notation to access the values stored in the keys of the dictionary <br><br>

**Example**
```
my_dict = {
    'an_integer': 1, 
    'a_float': 2.3, 
    'a_boolean': True, 
    'a_list': ['Another list']
}

print(my_dict[a_boolean])
# returns True
```

## Loops <a name="loops"></a>
Loops are an incredibly important in programming and allow you to apply actions to each object within a collection of objects. There are two loops we will be looking at; For and While loops

### While Loops <a name="while-loops"></a>
A While loop is reliant on Boolean conditions.. It will run while our condition is true and once it is false the while loop will stop. <br>
Be careful when using while loops that you don't get stuck in a never ending loop. Always make sure to change the condition within the loop, to make sure it stops running.  
<br><br>

**Example**
```
loop_control = 1
while loop_control <= 3:
    print('I am a while loop')
    loop_control += 1

#returns 
I am a while loop
I am a while loop
I am a while loop
```

Notice that we are adding 1 to the `loop_control` everytime the loop runs, so after the third time the loop runs, loop_control is less than or equal to 3, and the loop stops running. 

### For Loops <a name="for-loops"></a>
A For Loop needs to be given an iterable object and will cycle through each object within the iterable and return it for action. Strings, lists and dictionaries are all iterables in Python.<br><br>

**Example***
```
my_string = 'hello world!'

for letter in my_string:
    print(letter)

#returns 
h
e
l
l
o

w
o
r
l
d
!
```

Notice the word letter in the loop. This is a temporary name that I have give to describe what I am looping over in this string. This could be called anything, but I have used a meaningful name. Here is another example

**Example***
```
my_list_of_strings = ['hello', 'world', '!']

for word in my_list_of_strings:
    print(word)

#returns 
hello
world
!
```

We also don't have to give the iterable a name. we can do this as well

```
my_list_of_strings = ['hello', 'world', '!']

for word in my_list_of_strings:
    print(word)

#returns 
hello
world
!
```

These are just some basic loops, have a play around in Pycharm! How can we loop through dictionaries key, value pairs?

## Functions <a name="functions"></a>
All of the code so far has been written to be in a linear or line-by-line fashion. Functions allow us to write blocks of code that break our code down into smaller, modular chunks. They help us keep our code more organized and reusable. There is principle called DRY used in programming, standing for Don't Repeat Yourself! Writing functions helps us do that. To create a function, we use the `def` keyword, followed by our function name, and curly brackets. The curly brackets are used to store arguments or parameters we can pass through the function. Functions usually have a return value, which gets places in the return statement at the end of a function. Here are some examples <br><br>

**Example - function with no arguments**
```
def greeting():
    my_string = 'hello world!'
    return my_string
print(greeting())

#returns hello world!
```
Notice how in the print statement, I have the name of the function followed by curly brackets. This is how we invoke a function, also known as calling a function. If we do not call the function anywhere, nothing happens in the program. We must call the function to see the result. 

**Example - with arguments**
```
def greeting(first_name):
    my_string = f'hello {first_name}!'
    return my_string
print(greeting('jane'))

#returns hello jane!
```

Above I have given the name first_name to the argument/parameter we are passing into the function. You can name the argument anything, but again, be sure to use meaningful names so others can have a better understanding of what gets passed into the function. We pass the string we want into the function call, and that's how we get 'hello jane!' printed to the console. <br><br>

Another cool thing about functions, is that you can have as many arguments as you want! Read more about it [here](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)<br><br>

**Example - with multiple arguments**
```
def greeting(first_name, last_name,):
    my_string = f'hello {first_name} {last_name}!'
    return my_string
print(greeting('jane', 'doe'))

#returns hello jane doe!
```
