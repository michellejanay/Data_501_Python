# Python Object Oriented Programing 


## Table of Contents
- [Introduction](#introduction)
- [Abstraction](#abstraction)
- [Encapsulation](#encapsulation)
- [Inheritance](#inheritance)
- [Polymorphism](#polymorphism)

## Introduction <a name="introduction"></a>
### Motivation
Problems with Procedural Programming
- Data seperated from functions
- Lack of modularity
- High coupling
- Re-use difficult 
- Doesn't model the real world accurately 

Object Oriented Programming allows us to combine together the data elements and the operational elements into a signle unit, called a class.

Advantages of OOP
- Data functions combined
- Better modularity 
- Low coupling
- Re-use easier
- Closely models the real world

4 Principles
1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism

## Abstraction <a name="abstraction"></a>
A class contains 3 main things
1. Name
2. Data the class contains
3. A series of methods or functions that the class contains

Conventions
- Separate classes into a separate file
- Name initialized by capital letter
- class Classname, and then indented code inside class
- can define other methods as part of the constructor
- can create instances 

**Example**<br>
```
# customer class

class Customer: 
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
    def print(self):
        print(f'Customer: {self.first_name} {self.last_name}')  

cust.first_name = 'Michelle'
cust.last_name = 'Bee'  
cust.print()
# returns Customer: Michelle Bee
```

**Or**<br>
```
# customer class

class Customer:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    def print(self):
        print(f'Customer: {self.first_name} {self.last_name}')

cust1 = Customer1('Michelle', 'Bee')
cust1.print()
# returns Customer: Michelle Bee
```


## Encapsulation <a name="encapsulation"></a>
- Asks how do I work this thing
- Each class has a well-defined responsibility 
- Provide a simple, consistint interface to use the object
- Hide data and implementation details inside

**Convention:** if any feature of a class begins with an underscore, you should regard that as being a private feature, not something which is intended to be used by other pieces of code.

We can use Decorators

**Example**<br>
```
class Customer2:
    def __init__(self, fname, lname):
        self._first_name = fname
        self._last_name = lname
    def print(self):
        print(f'Customer: {self._first_name} {self._last_name}')
    @property
    def first_name(self):
        print('In the get method')
        return self._first_name
    @first_name.setter
    def first_name(self, new_first_name):
        print('In the setter')
        self._first_name = new_first_name

cust1 = Customer2('Michelle', 'Bee')
cust1.first_name = 'Jane'
# returns 
# In set method
# Customer: Jane Bee
```

The critical thing here is that now we can input logic into the set method, and we don't always have to allow the change to take place.

## Inheritance <a name="inheritance"></a>
- Different types 
- General and Specific
- Relationship hirearchy

1. Superclass/Base class - genrealized classes
2. Subclass/Derived class - specified classes

Both Superclass and Subclasses can be nested.


**Example**<br>
First we will set a person class
```
class Person:
    def __init__(self, fname, lname):
        self._first_name = fname
        self._last_name = lname

    def print(self):
        print(f"Customer: {self._first_name} {self._last_name}")

    @property
    def first_name(self):
        print("In the get method")
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        print("In the setter")
        self._first_name = new_first_name
```

Next, we will implement this class in two other classes

```
class Customer2(person.Person):
    def __init__(self, fname, lname, address):
        self._adress = address
        super().__init__(fname, lname)

    def print(self):
        print(f'Address: {self._adress}', end=' ')
        super().print()

cust1 = Customer2('Michelle', 'Bee', 'West Midlands')
cust1.print()
# returns Address: West Midlands Customer: Michelle Bee
```

and again

```
import person

class Employee(person.Person):
    def __init__(self, fname, lname, department):
        self._department = department
        super().__init__(fname, lname)
    def print(self):
        print(f'Department: {self._department}', end=' ')
        super().print()

emp = Employee('Michelle', 'Bee', 'Data Engineer')
emp.print()
# returns Department: Data Engineer Customer: Michelle Bee
```

The Customer and Employee class inherit the Person class, and add additional features to their respective classes. We can call methods/functions from the parent Person class using the super() method.

## Polymophirsm <a name="polymorphism"></a>
We may have several different kinds of objects, all of which are capable of dealing with the same kind of message.<br>
We can have a number of different classes, all of which are capable of dealing with the same kind of message or operation being called on them, but the classes themselves know how to perform that action for their particular case.

**Example**<br>
First we will set a person class
```
import random

if random.randint(0,1) == 0:
    my_person = Customer2('Michelle', 'Bee', 'West Midlands')
else:
    my_person = Employee('Michelle', 'Bee', 'Data Engineer')


my_person.print()
#returns either Address: West Midlands Customer: Michelle Bee or Department: Data Engineer Customer: Michelle Bee, depending on if the integer is 0 or 1
```