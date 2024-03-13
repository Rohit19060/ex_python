# Implement a function,multiply, taht takes 3 integer arguments a,b, and bound,
# if the restult of multiplying a and b is less than or equal to bound, the return the result;
# if the restult of multiplying a and b is greater than bound, the function rainsers a valueError exception with the following message: if a = 2,b= 5 and bound = 8, then the message must be "multiplication of 2 and 5 with bound 8 not possible"

# Implementation of the function will be tested by a provided code stub on serveral input files. Each input file contains serveral queries, and each query contains parameters for the function call. The function will be called with those parameters and the result of its exection will be printerd to the standard output by the provided code.

# Constraints:
# 1 <= the number of quereis in of test file <= 1000
# 1 <= a,b <= bound <= 1000000


# def multiply(a, b, bound):
#     if a * b <= bound:
#         return a * b
#     else:
#         raise ValueError(f"multiplication of {a} and {b} with bound {bound} not possible")

# if __name__ == "__main__":
#     a = 5
#     b = 2
#     bound = 23
#     print(multiply(a, b, bound))


# Arthur needs to perform 3 operation on an input - squaring a number, taking the square root of a number or sum of the input numbers. But the order of these opeation is not known beforehand. arthur realizes it to be a perfect situation to implement it using co-routinges and producer-filter-consumer patterns.
# Arthus has implemented the producer, consumer, and the pipeline and needs help to setup the accumulator (for summing the input), squarer (for squaring the input) and the rooter (for taking the square root of the number) co-routines.

# The accumulator should receive one number, should add that to the previously kept answer, and yeild that answer. The accumulator start at 0.
# The squaree should receive one number and yeild the square of that number.
# The rooter should receive one number and yeild the square root of that number. Note that you need to take the floor after doing the square root of the input.

# Take, for example, the order in which to implemetn these function to be order = [ square,accmulate] and the numbers to be nums = [1,2,3] with length n = 3. The complete function then is accumulator(square(nums)). After the furst number (1), the output is 1. After the second number (2), the output is 5. After the third number (3), the output is 14.

# Function description
# Compelte the co-routines accumulator, squaree, and rooter in the editor below.
# These co-routines do not have input and communicate completely througth the sub-routies pipeline.

# Constraints
# 1 <= n <= 100000
# 1 <= nums[i] <= 100000 where 0 <= i < n

# Input format for custom testing
# The first line contains an string, order, describing the order in which to perform the operations
# The next line contains an integer, n, denoting the number of elements in nums
# Each line i of the n subsequent lines (where 0 <= i < n) contains an integer describing nums[i]

# Sample Case 0
# Sample Input for custom testing

# STDIN                         Function
# [square,accumulate]            -> order = ['square', 'accumulate']
# 3                              -> n = 3
# 1                              -> nums = [1, 2, 3]
# 2
# 3

# Sample Output
# 1
# 5
# 14

# ctrl + +
# ctrl + mouse scrool wheel

# def testing():
#     x = 4
#     y = 5
#     z = add(x, y, 10, 20, 30)


# def greet(x):
#     print("hello " + x)
#     print("hello " + x)
#     print("hello " + x)


# def add(a, b, c, d, e):
#     return a+b + c + d + e


# modularazing the code
# testing()
# print(add(20, 30, 40, 50, 60))

# greet("Rohit Jain")
# greet("Ada")
# greet("Guido van Rossum")


# Homework
# 1. Write a function that takes a list of numbers and returns the sum of the numbers
# 2. Write a function that takes a list of numbers and returns the average of the numbers
# 3. Write a function that takes a list of numbers and returns the min of the numbers
# 4. Write a function that takes a list of numbers and returns the max of the numbers
# 5. Write a function that takes a number and give that the number is even or odd
# 6. Write a function that takes a number and give that the number is prime or not

# print(2 != 3)
# print(2 <= 3)
# print(2 < 3)
# print(2 >= 3)
# print(2 > 3)


# if ("Rohit" == "Rohit" and "Jain" == "Jain"):
#     print("3 is greater than 2")
#     print("Rohit is equanl to Rohit")

# If if ladder
# x = 5
# if (x > 3):
#     print("2 is greater than 3")
#     if (x > 5):
#         print("2 is greater than 4")
#         if (x > 10):
#             print("2 is greater than 5")

# Elif else if

# y = 7

# if (y == 2):
#     print("y is greater than x")
# elif (y == 3):
#     print("y is equal to x")
# elif (y == 4):
#     print("y is less than x")
# elif (not y == 5):
#     print("y == 5")
# else:
#     print("y in else")

# AND OR NOT

# 5 number
# a < b =>

# Q. Write a function that accept 5 argument and return the min of them


# def min_of_five(a, b, c, d, e):
#     x = a
#     if (x > b):
#         x = b
#     if (x > c):
#         x = c
#     if (x > d):
#         x = d
#     if (x > e):
#         x = e
#     return x


# print(min_of_five(1000, 256, 125, 40, 5))

# A Question for checking the understanding of the if else ladder
# Write a function that takes a number and returns the grade of the student according to the following criteria
# 1. If the number is greater than 90, return A
# 2. If the number is greater than 80, return B
# 3. If the number is greater than 70, return C
# 4. If the number is greater than 60, return D
# 5. If the number is greater than 50, return E
# 6. If the number is less than 50, return F

# Lists
# A list is a collection of items in a particular order

# words = ["Hello", "Worle", "Rohit", "Jain"]
# print(words)
# print(words[0])
# print(words[1])
# print(words[2])
# print(words[3])

# empty_list = []
# print(empty_list)

# things = ["strings", 1, 2.0, True, None, [1, 2, 3]]

# 2D, Multi-dimensional list
# print(things[1][0])
# print(things[5][0])

# str = "Hello World"
# print(str[0])
# print(str[1])

# words = ["Hello", "Worle", "Rohit", "Jain"]
# print(words)
# words[1] = words[3]
# print(words)

# nums = [1, 2, 3]
# print(nums + [4, 5, 6])
# print(nums * 3)

# x = "hello" + " world"
# print(x * 3)

# print("z" in x)

# print(not "z" in x)

# List Function

# Append
# words.append("5th Element")
# words.append("5th Element")
# words.append("5th Element")
# words.append("5th Element")
# print(len(words))

# insert
# .insert(index,element)
# words.insert(1, "2nd Element")
# print(words)

# print(x.index("h"))

# Give me a good question on lists

# Homework

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num = [1, 2, 3, 8, 5, 6, 7, 4, 9]
# Swap the 4 and 8 in the list
# print(num)

# print(num.index(4))
# print(num.index(8))
# print(num[3])
# print(num[7])
# num[3] = 8
# num[7] = 4


#

# print([1][3])

# words = ["Hello", "world", "Rohit", "Jain"]
# print(words)

# first_index = int(input("Enter the first index: "))
# second_index = int(input("Enter the second index: "))
# temp = words[first_index]
# print("Temp: ", temp)
# words[first_index] = words[second_index]
# print("Second Step")
# print(words)
# words[second_index] = temp
# print("Final Step")
# print(words)

# How many numbers does this loop execute
# i = 1

# while (i < 1000):
#     if i % 2 == 0:
#         print(str(i) + " is even")
#     else:
#         print(str(i) + " is odd")
#     i += 1

# Break and Continue (Skip)

# Break Example


# Table have 20 rows


# For Loop


# i = 0
# print("Length of words: ", i)
# while i < len(words):
#     print(words[i] + " is a word")
#     i += 1


# str = "Testing for loops"
# count = 0

# for x in str:
#     print(x)
#     if x == "t":
#         print("Got a t")
#         count += 1

# print(count)


# range


# this is a comment

# print("Hello World") # this is a new comment
# sdfasd f
# $asdf asdfasdf asdfa dsf

# print("hasdfa asdfasdf")

# import random

# for i in range(5):
#     print(random.randint(1, 1000))

# import math

# print(math.sqrt(144))

# for i in range(1, 10, 2):
#     print(math.sqrt(i))

# # from module_name import var
# print(math.factorial(5))

# import random

# print(random.randint(1,10000))

# for i in range(10):
#     print(random.randint(1,10))

# import math

# print(math.sqrt(144))
# print(math.factorial(10))
# print(math.ceil(10.6))
# print(round(10.6))
# print(math.floor(10.9))

# import random

# import math

# print(random.randrange(1, 100, 2))

# random_list = [random.randrange(1,100) for i in range(10)]

# print(random_list)


# # Print pi

# print(math.pi)


# pip
# Pip is a package manager for python modules, it is used to install and manage python modules like numpy, pandas, matplotlib, etc.

# import numpy as np

# print(np.pi)
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# arr = np.array([[1, 2, 3, 4, 5],
#                [1, 2, 3, 4, 5]])

# print(arr)

# arr = np.array((1, 2, 3))
# print(arr)


# Exceptions


# def add(a, b):
#     return a+b


# num1 = 9
# num2 = 0

# l1 = [1, 2, 3, 3, 4]

# queryResult = "asdfasdf"


# print("Hello World")

# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# try:
#     num = int(input("Enter a number: "))
#     print(num)
# except ValueError:
#     print("Invalid Input")


# RAWB
# try:
#     myfile = open("test.txt", "w")
#     msg = "Hello World"
#     myfile.write(msg)
# finally:
#     myfile.close()


# print(nums[4])

# Tuples Example


# List Slices

# nums = [4, 5, 6]
# msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
# print(msg)

# msg = f"Numbers: {nums[0]} {nums[1]} {nums[2]}"
# print(msg)

# msg = "{x} {y}".format(y=12, x=5)
# print(msg)

# Python program to find N largest elements from a list

# def Nmaxelements(list1, N):
#     final_list = []

#     for i in range(0, N):
#         max1 = 0
#         for j in range(len(list1)):
#             print("j: ", j)
#             if list1[j] > max1:
#                 max1 = list1[j]
#         list1.remove(max1)
#         final_list.append(max1)
#     print(final_list[-1])

# def add(x,y):
#     return x+y

# list = [2, 6, 41, 85, 0, 3, 7, 6, 10]

# list2 = [85]

# N = 5

# # Calling the function
# Nmaxelements(list, N)

# def apply_twice(func, arg):
#     return func(func(arg))

# def add_fine(x):
#     return x + 5

# print(apply_twice(add_fine, 10))


# def pure_funcion(x,y):
#     temp = x + 2*y
#     return temp / (2*x + y)

# print(pure_funcion(2,3))

# some_list = []

# def impure(arg):
#     some_list.append(arg)

# def my_func(func, arg):
#     return func(arg, arg, arg)


# print(my_func(lambda x, y, z: (x*2) + (y*2) + (z*2), 5))


# def polynomian(x):
#     return x ** 2 + 5*x + 4


# print(polynomian(-4))

# # labmda
# print((lambda x, y: x**2 + 5*x + 4)(-4, 5))


# def double(x): return x * 2


# print(double(7))


# def add_five(x):
#     return x + 5


# num = [11, 22, 33, 44, 55]
# restult = list(map(add_five, num))


# num = [11, 22, 33, 44, 55]
# result = list(map(lambda x: x+5, num))

# print(result)


# result = list(filter(lambda x: x % 2 == 0, num))
# print(result)


# def countdown():
#     i = 5
#     while i > 0:
#         yield i
#         i -= 1

# for i in countdown():
#     print(i)

# def numbers(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i

# print(list(numbers(11)))

# def decorX(func):
#     def wrap():
#         print("============")
#         # Logging
#         # Analytics
#         func()
#         # Logging
#         # Analytics
#         print("============")
#     return wrap

# @decorX
# def print_text():
#     print("Hello World")

# print_text()

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x-1)


# print(factorial(10))


# def is_even(x):
#     if x == 0:
#         return True
#     else:
#         return is_odd(x-1)

# def is_odd(x):
#     return not is_even(x)

# print(is_odd(17))
# print(is_even(23))

# num_set = {1, 2, 3, 4, 5, 5}
# print(num_set)

# word_set = set(["spam", "eggs", "sausage"])
# print(word_set)

# print(3 in num_set)
# print("spam" not in word_set)
# print(len(word_set))
# num_set.add(-7)
# num_set.remove(3)
# num_set.pop()
# print(num_set)

# Uninon, | intersection, & difference, - symmetric_difference, ^
# print(num_set | {3, 4, 5, 6})
# print(num_set & {3, 4, 5, 6})
# print(num_set - {3, 4, 5, 6})
# print(num_set ^ {3, 4, 5, 6})
# print(num_set)


# Itertools

# from itertools import count, accumulate, takewhile,product,permutations, combinations

# for i in count(3):
#     print(i)
#     if i >= 11:
#         break


# nums = list(accumulate(range(8)))
# print(nums)
# print(list(takewhile(lambda x: x <= 6, nums)))


# letter = ("A","B","C")

# print(list(product(letter,range(2))))
# print(list(permutations(letter)))
# print(list(combinations(letter,2)))

# What is the result of this code?
# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3} & nums
# nums = filter(lambda x: x > 1, nums)
# print(len(list(nums)))

# What is the result of this code?
# def power(x, y):
# if y == 0:
# return 1
# else:
# return x * power(x, y-1)
# print(power(2, 3))

# Fill in the blanks to calculate the expression x*(x+1) using an anonymous function and call it for the number 6.
# a = ( __ x: x __ (x+1))
# ___
# print(a)

# Fill in the blanks to leave only even numbers in the list.
# nums = [1, 2, 8, 3, 7]
# res = list(__ (__x:x%__==0,nums)
# print(res)


# class Cat:
#     def __init__(self, color, legs):
#         self.color = color
#         self.legs = legs

#     def meow(self):
#         print("Meow!")
#         print(self.color)
#         print(self.legs)


# felix = Cat("ginger", 4)
# print(felix.color)
# print(felix.legs)
# felix.meow()
# rover = Cat("dog-colored", 4)
# stumpy = Cat("brown", 3)

# class Student:
#     legs = 2
#     def __init__(self, name, subjects, age, roll_no):
#         self.name = name
#         self.subjects = subjects
#         self.age = age
#         self.roll_no = 6


#     def is_adult(self):
#         return self.age >= 18

#     def is_votable(self):
#         if(self.age >= 18):
#             print("You can vote")
#             return True
#         else:
#             print("You cannot vote")
#             return False

# rohit = Student("Rohit Jain", ["Maths", "Physics", "Chemistry"], 15, 1)

# print("Name: ", rohit.name)
# print(rohit.is_adult())
# rohit.is_votable()

# ada = Student("Ada", ["Maths", "Physics", "Chemistry"], 30, 2)


# print("Name: ", ada.name)
# print(ada.xys)
# print(ada.legs)
# print(ada.is_adult())
# ada.is_votable()


# Base class, Super Class, Parent Class
# class Animal:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color


# Derived Class, Sub Class, Child Class
# class Cat(Animal):
#     def meow(self):
#         print("meow...")


# class Dog(Animal):
#     def bark(self):
#         print("woof!")


# fido = Dog("Fido", "brown")
# print(fido.name)
# fido.bark()


# class A:
#     def method(self):
#         print("A Method")


# class B(A):
#     def another_method(self):
#         super().method()
#         print("B Method")


# class C(B):
#     def third_method(self):
#         super().method()
#         print("C Method")


# c = C()
# c.third_method()
# c.another_method()
# c.method()

# C().third_method()

# Create a student class and couple of inherited classes from student class
# 1. Create a student class with name, age, roll_no, subjects
# 2. Create a method is_adult which returns true if the student is an adult
# 3. Create a sub class for elementary school students
# 4. Create a sub class for high school students


# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __sub__(first, second):
#         return Vector2D(first.x + second.x + 2, first.y + second.y + 2)

#     def __lt__(first, second):
#         return Vector2D(first.x < second.x, first.y < second.y)


# first = Vector2D(5, 7)
# second = Vector2D(3, 9)

# result = first < second

# print(result.x)
# print(result.y)


# __add__ for +
# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |

# __lt__ for <
# __le__ for <=
# __eq__ for ==
# __ne__ for !=
# __gt__ for >
# __ge__ for >=

# __len__ for len()
# __getitem__ for indexing
# __setitem__ for assigning to indexed values
# __delitem__ for deleting indexed values
# __iter__ for iteration over objects (e.g., in for loops)
# __contains__ for in


# import random


# class VagueList:
#     def __init__(self, cont):
#         self.cont = cont

#     def __getitem__(self, index):
#         return self.cont[index + random.randint(-1, 1)]

#     def __len__(self):
#         return random.randint(0, len(self.cont)*2)

#     def __setitem__(self, index, value):
#         print("Assigning")
#         self.cont[index] = value


# vague_list = VagueList(["A", "B", "C", "D", "E"])
# print(vague_list.cont[2])
# print(len(vague_list))
# print(len(vague_list))
# print(vague_list[2])
# print(vague_list[2])
# vague_list[2] = "Rohit"
# print(vague_list[2])

# __str__ for str()


# class Student:
#     def __init__(self, mark1, mark2, mark3):
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3

#     def __add__(self, other):
#         return Student(
#             self.mark1 + other.mark1, self.mark2 + other.mark2, self.mark3 + other.mark3
#         )

#     def __str__(self):
#         print("Triggered")
#         return f"Sum of marks: {self.mark1 + self.mark2 + self.mark3}"

#     def __mul__(self, other):
#         return (self.mark1 + self.mark2 + self.mark3) / 3

#     def __len__(self):
#         return self.mark1 + self.mark2


# c1 = Student(10, 20, 30)
# c2 = Student(20, 30, 40)
# c3 = Student(20, 30, 40)
# c4 = Student(20, 30, 40)

# print(f"Sum of marks: {c1 + c2 + c3 + c4}")
# print(f"Average of marks: {c2 * c2}")


# a = 42  # Create object <42>
# b = a # Increase ref. count  of <42>
# c = [a] # Increase ref. count  of <42>

# del a # Decrease ref. count  of <42>
# b = 100  # Decrease ref. count  of <42>
# c[0] = -1  # Decrease ref. count  of <42>


# Data Hiding


# class Queue:
#     __egg = 7

#     def print_egg(self):
#         print(self.__egg)

#     def __init__(self, contents):
#         self._hiddenlist = list(contents)

#     def push(self, value):
#         self._hiddenlist.insert(0, value)

#     def pop(self):
#         return self._hiddenlist.pop(-1)

#     def __repr__(self):
#         # return "Queue({})".format(self._hiddenlist)
#         return f"Queue({self._hiddenlist})"


# x = Queue([1, 2, 3])
# print(x)
# x.push(0)
# print(x)
# x.pop()
# print(x)
# x.print_egg()
# print(x.__egg)
# print(x._Queue__egg)


# ClassMethods and StaticMethods

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height

#     @classmethod
#     def new_square(cls, side_length):
#         print("New Square")
#         return cls(side_length, side_length)


# rect = Rectangle(3, 4)
# square = Rectangle.new_square(5)
# print(square.calculate_area())

# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings

#     @staticmethod
#     def validate_toppings(topping):
#         if topping == "pineapple":
#             raise ValueError("No pineapples!")
#         else:
#             print("Valid Topping")

# Pizza.validate_toppings("asdfasdf")

# ingrediants = ["cheese", "pineapple", "spam"]

# if all(Pizza.validate_toppings(i) for i in ingrediants):
#     pizza = Pizza(ingrediants)


# class Array20:
#     def __init__(self, lst):
#         self.lst = lst

#     @classmethod
#     # for validation the list always have 20 elements
#     def from_input(cls, list):
#         # if element is not 20 then add rest of the elements as 0
#         if len(list) < 20:
#             list.extend([2] * (20 - len(list)))
#         else:
#             list = list[:20]
#         return cls(list)


# arr = Array20.from_input([5, 1, 2])
# arr1 = Array20.from_input([5])
# print(arr.lst)
# print(arr1.lst)

# Number System


# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#         self._pineapple_allowed = False

#     @property
#     def pineapple_allowed(self):
#         return self._pineapple_allowed

#     @pineapple_allowed.setter
#     def pineapple_allowed(self, value):
#         password = input("Enter the password: ")
#         if password == "123":
#             self._pineapple_allowed = value
#         else:
#             raise ValueError("Alert! Intruder!")

#     @property
#     def x(self):
#         print("Triggered")


# pizza = Pizza(["cheese", "tomato"])
# print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True
# print(pizza.pineapple_allowed)
# print(pizza.x)


# def say(noun):
#     return f"Hello {noun}"


# def examine(noun):
#     if noun in GameObject.objects:
#         return GameObject.objects[noun].get_desc()
#     else:
#         return "There is no {} here.".format(noun)


# def hit(noun):
#     if noun in GameObject.objects:
#         thing = GameObject.objects[noun]
#         if type(thing) == Goblin:
#             thing.health = thing.health - 1
#             if thing.health <= 0:
#                 msg = "You killed the goblin!"
#             else:
#                 msg = "You hit the {}".format(thing.class_name)
#         else:
#             msg = "There is no {} here.".format(noun)
#         return msg


# verb_dict = {
#     "say": say,
#     "examine": examine,
#     "hit": hit,
# }


# def get_input():
#     command = input(": ").split()
#     verb_word = command[0]
#     if verb_word in verb_dict:
#         verb = verb_dict[verb_word]
#     else:
#         print("Unknown verb {}".format(verb_word))
#         return

#     if len(command) >= 2:
#         noun_word = command[1]
#         print(verb(noun_word))
#     else:
#         print(verb("nothing"))


# class GameObject:
#     class_name = ""
#     desc = ""
#     objects = {
#     }

#     def __init__(self, name):
#         self.name = name
#         GameObject.objects[self.class_name] = self

#     def get_desc(self):
#         return self.class_name + "\n" + self.desc


# class Goblin(GameObject):
#     def __init__(self, name):
#         self.class_name = "goblin"
#         self.health = 3
#         self._desc = "A foul creature"
#         super().__init__(name)

#     @property
#     def desc(self):
#         if self.health >= 3:
#             return self._desc
#         elif self.health == 2:
#             health_Line = "It has a wound on its knee"
#         elif self.health == 1:
#             health_Line = "Its left arm has been cut off!"
#         elif self.health <= 0:
#             health_Line = "It is dead"
#         return self._desc + "\n" + health_Line

#     @desc.setter
#     def desc(self, value):
#         self._desc = value


# goblin = Goblin("Gobbly")


# while True:
#     get_input()

# import re

# pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"

# email = input()

# match = re.match(pattern, email)

# if match:
#     print("Valid Email")
# else:
#     print("Invalid Email")


# Write a regular expression that matches a string containing a sequence of three or more consecutive vowels (a, e, i, o, u) or consonants.

# import re

# pattern = r"[aeiouAEIOU]{3,}"

# if re.search(pattern, "axee"):

#     print("Match 1")

# if re.search(pattern, "aeee"):
#     print("Match 2")

# if re.search(pattern, "aeee"):

#     print("Match 3")

# How would you extract Url from a string

# import re

# pattern = r"https?://[a-zA-Z0-9.-]+/[a-zA-Z0-9.-]+"

# url = input()

# match = re.match(pattern, url)

# if match:

#     print("Valid Url")

# else:

#     print("Invalid Url")


# import re

# Example string
# example_string = "This is a sample string with a URL https://www.example.com and another URL http://example2.com"

# # Regular expression pattern to extract URLs
# url_pattern = re.compile(r'https?://\S+')

# # Find all URLs in the string
# urls = re.findall(url_pattern, example_string)

# # Print the extracted URLs
# for url in urls:
#     print(url)


# # Example pattern to match strings containing three consecutive repeating characters
# pattern = re.compile(r"(\d)\1{2}")

# # Example string to test the pattern
# example_string = "111223333444455555666"

# # Find all matches in the string
# matches = re.findall(pattern, example_string)

# # Print the matches
# print(matches)

# How would you match a string that starts with "hello" and ends with "world"?

# Write a regular expression that matches a 10-digit phone number, allowing for an optional country code at the beginning.


# +91 123-456-7890
# +123 123-456-7895
# +1 123-456-7894
# 9529916394
# import re

# from numpy import true_divide

# pattern = r"^(\+[0-9]{1,3} )?[0-9]{3}-[0-9]{3}-[0-9]{4} || [0-9]{10}$"

# assert re.match(pattern, "+91 123-456-7890")
# assert re.match(pattern, "+123 123-456-7895")
# assert re.match(pattern, "+1 123-456-7894")
# assert re.match(pattern, "9529916394")
# assert re.match(pattern, "+91 9529916394")


# # How would you extract all the words from a sentence, ignoring punctuation and special characters?

# pattern = r"[a-zA-Z]+"
# example_string = "This is a sample string with a URL https://www.example.com and another URL http://example2.com"
# matches = re.findall(pattern, example_string)


# #  How would you extract the URLs?

# pattern = r"https?://\S+"

# matches = re.findall(pattern, example_string)

# # Create a regular expression that matches strings containing a repeating sequence of characters (e.g., "abab", "1212", "abcabc").

# pattern = r"(\w+)\1"

# assert re.match(pattern, "aba12aba12")
# assert re.match(pattern, "a12a12")
# assert re.match(pattern, "abcabc")
# # assert re.match(pattern, "axbxaxbc")


# # Write a regular expression that matches strings containing a specific number of consecutive repeating characters (e.g., "111", "22", "333").

# pattern = r"(\w)\1{2}"

# assert re.match(pattern, "111")
# # assert re.match(pattern, "22")
# assert re.match(pattern, "333")
# assert re.match(pattern, "3334")
# assert re.match(pattern, "44444")

# print("Matched all")

# # spamspamspam

# pattern = r"spam"

# assert re.match(pattern, "spasdfasdf")

# if re.match(pattern,"eggspamsausagespam"):
# # Match is for matching the pattern at the start of the string and returns the match object
#     print("Match")
# else:
#     print("No Match")

# # search is for searching the pattern in the string and returns the first occurance of the pattern
# if re.search(pattern,"eggspamsausagespam"):
#     print("Match")
# else:
#     print("No Match")

# pattern = r"spam"
# print(re.findall(pattern, "eggspamsausagespam"))
# print(re.search(pattern, "eggspamsausagespam"))
# print(re.match(pattern, "spameggspamsausagespam"))
# match = re.match(pattern, "spameggspamsausagespam")
# match1 = re.search(pattern, "spameggspamsausagespam")
# # findall is for searching the pattern in the string and returns all the occurances of the pattern

# print(match.group())
# print(match.start())
# print(match.end())
# print(match.span())
# print(match1.group())
# print(match1.start())
# print(match1.end())
# print(match1.span())

# # sub

# # re.sub(patter, replacement, string,count)

# str = "My Name is Rohit. HI Rohit"

# pattern = "Rohit"

# newStr = re.sub(pattern, "Rohit Jain", str, 10)
# print(newStr)


# # 7. Write a regular expression that matches a string containing a sequence of three or more consecutive vowels (a, e, i, o, u) or consonants.

# pattern = r"[a-z]{3,}"

# assert re.search(pattern, "aee")
# assert re.search(pattern, "aeee")
# assert re.search(pattern, "aeee")

# pattern = r"g..y"

# assert re.match(pattern, "gbey")
# assert re.match(pattern, "gray")
# # assert re.match(pattern, "blue")

# patters = r"[G-P][aeiou]"

# assert re.match(patters, "Ha")
# # assert re.match(patters, "ee")
# # assert re.match(patters, "ia")
# # assert re.match(patters, "grey")

# pattern = r"[^1-5][0-9]"


# pattern = r"g*"

# assert re.match(pattern, "g")
# assert re.match(pattern, "ggggggggg")
# assert re.match(pattern, "")

# pattern = r"g+"

# assert re.match(pattern, "g")
# assert re.match(pattern, "ggggggggg")
# assert re.match(pattern, "ggg")


# pattern = r"ice-?cream"

# assert re.match(pattern, "ice-cream")
# assert re.match(pattern, "icecream")
# # assert re.match(pattern, "ice--cream")


# pattern = r"9{1,3}$"

# assert re.match(pattern, "9")
# assert re.match(pattern, "999")
# # assert re.match(pattern, "9999")

# pattern = r"egg(spam)*"

# assert re.match(pattern, "egg")
# assert re.match(pattern, "eggspam")
# assert re.match(pattern, "eggspamspamspam")
# # assert re.match(pattern, "spam")

# email = "rohit@gmail.com"

# pattern = r"a(c)(de)(f(g)h)i"

# match = re.match(pattern, "abcdefghi")
# match = re.match(pattern, "abcdefghijklmnop")
# if match:
#     print(match.group())
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))
#     print(match.group(4))
#     print(match.groups())


# pattern = r"gr(a|e)y"

# assert re.match(pattern, "gray")
# assert re.match(pattern, "grey")
# # assert re.match(pattern, "griy")

# pattern = r"(.+) \1"

# assert re.match(pattern, "word word")
# assert re.match(pattern, "?! ?!")
# assert re.match(pattern, "abcde abcde")
# # assert re.match(pattern, "abc cde")

# # Ternary Operator

# # condition_if_true if condition else condition_if_false

# is_something = False
# a = 54

# x = 1 if (a == 54) else 0

# x = 0
# if a == 54:
#     x = 1

# # print(x)

# status = 1
# y = "logout" if status == 1 else "login"

# # x == y ? x = 1 : x = 0
# # inline if

# # print(x)

# numbers = (1, 2, 3)
# a, b, c = numbers

# print(a)
# print(b)
# print(c)

# listx = [1, 2, 3]
# a, b, c = listx

# print(a)
# print(b)
# print(c)


# x = 5
# y = 10
# x, y = y, x

# print(x)

# a, b, *c, d, e = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)


def xFunction(named_args, second, *args, y=7):
    print(named_args)
    print(second)
    print(args)
    print(y)
    # print(args[0])


# def yFunction(x, y, food="spam"):
#     print(x)
#     print(y)
#     print(food)


# xFunction(1, [2, 3], [4, 5, 6, 7, 8, 9, 10], y=8)
# yFunction(1, 2)
# yFunction(5, 8, "egg")


# def function(x, z, *argums, y=7):
#     print(x)
#     print(y)
#     print(z)
#     print(argums)


# function(3, 4, 43, 3, 3, 22, 4, 4, 4)


# def my_funx(x, y=7, *args, **kwargs):
#     print(x)
#     print(y)
#     print(args)
#     print(kwargs)


# my_funx(2, 3, 4, 5, 6, 7, a=7, b=8, c=8)

# Else Updates

# for i in range(10):
#     if i == 999:
#         break
# else:
#     print("Unbroken 1")

# for i in range(10):
#     if i == 5:
#         break
# else:
#     print("Unbroken 2")


# try:
#     print(1)
# except ZeroDivisionError:
#     print(2)
# else:
#     print(3)

try:
    print(1 / 0)
except ZeroDivisionError:
    print(4)
else:
    print(5)
