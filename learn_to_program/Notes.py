

***********************************************
*********************WEEK 2********************
***********************************************

Recipe for Designing Functions:
1. Header
2. Type Contract
3. Description
4. Examples (normally 1st step in Design recipe)
5. Body
6. Test

def function(parm1, parm2):  #Header
	''' (param1, parm2) -> number  #Type Contract
	
	Description goes here
	>>> function(12, 34) # Example 1
	expected results
	>>> function (4, 9) # Example 2
	expected results
	'''
	return parm1 + parm2 # Body of function

function(32, 43)	##Test

def perimeter (side1, side2, side3):
	''' (number, number, number) -> number

	Return the perimeter of the triangle with sides of
	length side1, side2, side3.

	>>> perimeter(3, 4, 5)
	12
	>>> perimater(10.5, 6, 9.3)
	25.8
	'''
	return side1 + side2 + side3

def semiperimeter (side1, side2, side3):
	''' (number, number, number) -> float

	Return the semiperimeter of a triangle with sides of
	length side1, side2, and side3. 

	>>> semiperimeter(3, 4, 5)
	6.0
	>>> semiperimeter(10.5, 6, 9.3)
	12.9
	'''
	return perimeter(side1, side2, side3) / 2 #calls perimeter function 


def convert_to_celsius(f):
    '''(number) -> float

    Return the fahrenheit(f) temperature to celsius temperature.
    >>> convert_to_celsius(32)
    0.0
    >>> convert_to celsius(212)
    100.0
    '''
    return (f - 32) * 5 / 9

def area(base, height):
	'''(number, number) -> fload

	Return the area of a triangle with given base & height
	>>> area(10, 40)
	200.0
	>>> area(3.4, 7.5)
	12.75
	'''
	return base * height / 2

#if we have 2 triangles, one has a width of 3.8 & height of 7
#the second a width of 3.5 & height of 6.8
#to determine which has a bigger area
max(area(3.8, 7), area(3.5, 6.8))
13.29999999999999 # returns the float of the biggest triangle
# Running each 'area' individually will show the 1st is the max
area (3.8, 7)
13.29999999999999
area(3.5, 6.8)
11.9

(usa_city_temperature(Seattle), convert_to_celsius(Seattle))

def convert_to_minutes(num_hours):
	'''(int) -> int
	Return the number of minutes there are in num_hours.
	>>> convert_to_minutes(2)
	120
	'''
	minutes = num_hours * 60
	return minutes
minutes_2 = convert_to_minutes(2)
minutes_3 = convert_to_minutes(3)

***********************************************
*********************WEEK 3********************
***********************************************
*Functions, Variables, and Call Stack

def convert_to_minutes(num_hours):
	'''(int) -> int
	Return the number of minutes there are in num_hours.
	>>> convert_to_minutes(2)
	120
	'''
	minutes = num_hours * 60

def convert_to_seconds(num_hours):
	''' (int) -> int
	Return the number of seconds there are in num_hours hours.
	>>> convert_to_seconds(2)
	7200
	'''

	minutes = convert_to_minutes(num_hours)
	seconds = minutes * 60
	return seconds
seconds = convert_to_seconds(2)

# When a function exits, the fram for the function is erased, and 
# control is passed back to the statement containing the function
# call. The faluve of that function call is whatever was returned 
# by the function.

==================================
	*Boolean Values
++++++ Comparison Operators +++++++
< 	less than
> 	greater than
== 	equal to
>=	greater than or equal to
<= 	less than or equal to
!=	not equal to

===============================
++++++ Logical Operators ++++++
not
and
or

grade = 50
grade >= 50
	True
not (grade >= 50) # Paren evaluated first=True. not True = False
	False
not not (grade >= 50)
	True

grade2 = 70
(grade >= 50) and (grade2 >= 50) 
	True
grade = 40
(grade >= 50) and (grade2 >= 50)
	False
grade = 80
grade2 = 40
(grade >= 50) and (grade2 >= 50)
	False

grade = 80
grade2 = 90
not grade >= 50 or grade2 >= 50
	True
not (grade >= 50 or grade2 >= 50)
	False
(not grade >= 50) or grade2 >= 50
	True
#Use parenthesis to ensure the operations go in the order you
# want them to.
(4 != 4) or (2 > 3)
	False

((math_grade >= 50 and bio_grade >= 50 and cs_grade >= 50) and (math_grade >= 80 or bio_grade >=80 or cs_grade >= 80))
	True
# AND evaluates to AND if, and only if, both operands are True.
# or evaluates to True if, and only if, both operands are True.

++++++ Convert between int, str, float ++++++
three = str(3)
three
	'3'
three * 7
	'3333333'
int(three * 5)
	33333 # this is an INT. notice no quotes
str(int(three * 5))
	'33333'
float('456')
	456.0

==========================================
++++++ Import Non Builtin Functions ++++++
import math
dir(math) # lists the functions built into the math module
help(math.sqrt)
	Help on built-in function sqrt in module math:

	sqrt(...)
    	sqrt(x)
    	Return the square root of x.


_-_-_-everything below would be in triangle.py 
import math
def area(base, height):
	'''(number, number) -> fload

	Return the area of a triangle with given base & height
	>>> area(10, 40)
	200.0
	>>> area(3.4, 7.5)
	12.75
	'''
	return base * height / 2
def perimeter (side1, side2, side3):
	''' (number, number, number) -> number

	Return the perimeter of the triangle with sides of
	length side1, side2, side3.

	>>> perimeter(3, 4, 5)
	12
	>>> perimater(10.5, 6, 9.3)
	25.8
	'''
	return side1 + side2 + side3

def semiperimeter (side1, side2, side3):
	''' (number, number, number) -> float

	Return the semiperimeter of a triangle with sides of
	length side1, side2, and side3. 

	>>> semiperimeter(3, 4, 5)
	6.0
	>>> semiperimeter(10.5, 6, 9.3)
	12.9
	'''
	return perimeter(side1, side2, side3) / 2 
def area_hero(side1, side2, side3):
	''' (number, number, number) -> float
	
	Return the area of a trangle with sides of length
	side1, side2, side3

	>>> area_hero(3, 4, 5)
	6.0
	>>> area_hero(10.5, 6, 9.3)
	27.73168584850189
	'''
	semi = semiperimeter(side1, side2, side3)
	area = math.sqrt(semi * (semi * side1) * (semi * side2) * (semi * side3))
	return area

===========================
++++++ if Statements ++++++
Ex. 3:00am = 3.0
Ex. 14:30 = 14.5
Times we working on are 0.0 < time < 24
	This is a precondition
	precondition: the condition under which a function is intended to work.

def report_status(scheduled_time, estimated_time):
	''' (number, number) -> str

	Return the flight status(on time, early, delayted) for a flight that was scheduled to arrive at a scheduled_time, but is not estimated to arrive at estimated_time.
	
	Pre-condition: 0.0 <= scheduled_time < 24 and 0.0 <= estimated_time < 24

	>>> report_status(14.3, 14.3)
	'on time'
	>>> report_status(12.5, 11.5)
	'early'
	>>> report_status(9.0, 9.5)
	'delayed'
	'''

	if scheduled_time == estimated_time:
		return 'on time'
	elif scheduled_time < estimated_time:
		return 'delayed'
	else:
		return 'early'

# if a function ends without a return statement being executed, that function will return a None (NoneType)
def is_even(num):
	''' (int) -> bool

	Return whether num is even

	>>> is_even(4)
	True
	>>> is_even(77)
	False
	'''
	if num % 2 == 0:
		return True
	else:
		return False
----OR----
	return num % 2 ==0

precipitation = True
temperature = -3
if precipitation:
	if temperature >0:
		print('Bring your umbrella')
	else:
		print('wear your boots and coat')
----OR----
if precipitation and temperature > 0:
	print('Bring your umbrells')
elif precipitation:
	print('wear your boots and coat')


***********************************************
******************** WEEK 4 *******************
***********************************************

Capital letters are not equal to their lowercase version.
Values of different types (int, str) can be compared for equality. 
Values of different types usually cannot be compared for ordering. (Although ints and floats can be compared)
'a' <= 'A'	False
'A' <= 'B'	True
'abracadabra' < 'ace'	True
'abracadabra' > 'ace'	False
',' < '3'	True
'cad' in 'abracadabra'	True
'c' in 'aeiou'	False
'' in 'abe'	True

len('')		0
len('abracadabra')		11
len('bwa' + 'ha' * 10)	23

================================
++++++ Indexing & Slicing ++++++

Index: a position within a string
s= 'Learn to Program'
s[0]	'L'	# start at index 0 (not 1)
s[1]	'e'
s[2]	'a'
s[-1]	'm'	# can start from end by using negative numbers
s[-2]	'a'
s[-3]	'r'
Slicing: a substring of a string from a start index up to but not including the end index.
s[0:5]	'Learn' #includes string from 0-4, not 5
s[6:8]	'to'
s[9:16]	'Program'
OR s[9:len(s)]	'Program'
OR s[9:]	'Program' #trailing index omitted, thus goes to end
s[:8]	'Learn to'
s[:]	'Learn to Program'
s[1:8]	'earn to'	OR
s[1:-8]	'earn to'	OR
s[-15:-8]	'earn to'

Strings are immutible. You cannot change slices or indexes.
If you want to change the string:
s = s[:5] + 'ed' + s[5:]	'Learned to Program'
	This creates a new string, does not modify the old str

==================================================
++++++ Methods: Functions inside of objects ++++++
module: math
	function: sqrt or factorial
Values, also known as objects can contain functions as well
'Method': a function inside of objects
Form of a method call:
object.method(arguments)

string methods

import the module
call the function inside of the method
white_rabbit = 'Im late, Im late. For an important date!'
white_rabbit.lower()	'im late. im late. for an important date!'
	this produces a new string.
dir(white_rabbit) will produce the methods available
dir(str)	will give the same results
help(str.lower) 
help(str.count)
	white_rabbit.count('ate') results in 3
computer.capitalize()	'Computer'
white_rabbit.find('late')	3 #Find the index of the first 			occurence
white_rabbit.find('late', 7)	12
white_rabbit.rfind
.lstrip()	removes white space on the left
.rstrip()	removes white space from the right
.strip()
	None of these affects the original string, just create a new one.

===============================
++++++ for loop over str ++++++
s = 'Hi There!'
for char in s:
	print (char)
H
i
 
T
h
e
r
e
!

def collect_vowels (s):
    ''' (str) -> str
    Return the vowels in s. Does not include 'y' as a vowel.
    >>> collect_vowels ('Happy Anniversary!')
    aAiea
    >>> collect_vowels('xyz')
    ''
    '''
    vowels = ''
    for i in s:
        if i in 'aeiouAEIOU':
            vowels = vowels + i
    return vowels

def count_vowels(s):
    ''' (str) -> int
    Return the number of vowels in s. Does not includ "y" as vowel.
    >>> count_vowels ('Happy Anniversary!')
    5
    >>> count_vowels ('xzy')
    0
    '''
    num_vowels = 0
    for i in s:
        if i in 'aeiouAEIOU':
            num_vowels = num_vowels + 1
    return num_vowels

===================================
++++++++++IDLEs Debugger+++++++++++

Python visualizer, does nto allow import statments and stops
after 500 steps.

IDLE has a built in Debugger


***********************************************
******************** WEEK 5 *******************
***********************************************

===================================
++++++++++WHILE Loops++++++++++++++
While loops will run until loop condition becomes false.
Example
num = 2
while num < 50:
	num = num * 2
	print(num)
4
8
16
32
64
The loop will stop at 64 because the number before was 32, which is less than 50. Thus the loop runs 1 more time.
iteration = execution of the loop body

s = 'hello'
for char in s:
	print(char)
i = 0
while not (s[i] in 'aeiouAEIOU'):
	print(s[i])
	i = i + 1
RESULT: h

------------OR
s = 'There'
i = 0
while not (s[i] in 'aeiouAEIOU'):
	print(s[i])
	i = i + 1
RESULT: Th

The loop will run until False. Some errors will occur if index is out of range. Get around this by setting a limit
i = 0
s = 'xyz'
while i < len(s) and not (s[i] in 'aeiouAEIOU'):
	print(s[i])
	i = i + 1
RESULT: xyz

def up_to_vowel(s):
	''' (str) -> str

	Return a substring of s from index 0 up to but not including the first vowel in s. 
	Accumulate the consonents before the 1st vowel

	>>> up_to_vowel('hello')
	'h'
	>>> up_to_vowel('there')
	'th'
	>>> up_to_vowel('cspqrt')
	'cspqrt'
	'''
	before_vowel = ''
	i = 0
	while i < len(s) and not (s[i] in 'aeiouAEIOU'):
		before_vowel = before_vowel + s[1]
		i = i + 1
	return before_vowel


def get_answer(prompt):
	''' (str) - > str
	Use prompt to ask user for a 'yes' or 'no' answer & continue asking until the user gives the valid response. Return the answer.
	
	'''
	answer = input(prompt)

	while not (answer == 'yes' or answer == 'no'):
		answer = input(prompt)
	return answer
: Run this by 'get_answer("Are you tired? yes or no? ")'
:: RESULT: Are you tired? yes or no? 
if you answer maybe, youll be prompted again.

def last_vowel(s):
    """(str) -> str
    Return the last vowel in s if one exists; otherwise, return None.
    >>> last_vowel("cauliflower")
    "e"
    >>> last_vowel("pfft")
    None
    """
    i = len(s) - 1
    while i >= 0:
         if s[i] in 'aeiouAEIOU':
             return s[i]
         i = i - 1
   return None


===================================
+++++++++++++Comments++++++++++++++

Comments are used by placing a '#' character in the beginning of the line. Python will ignore these lines.

Using the before_vowel function above.
0123456
zymurgy
# before_vowel contains all the characters found in s[0:i].
so s is 
s[0:7]	zymurgy
s[0:6]	zymurg
s[0:5]	zymur
s[0:4]	zymu 
s[0:3]	zym
s[0:2]	zy
s[0:1]	z
s[0:0]	''

Use comments to tell the purpose of the item.

===================================
+++++++++++++Type list++++++++++++++
A list:
grades = [80, 90, 70]
so
grades[0]	=	80
grades[1]	=	90
grades[1:2]	=	[90]
grades[0:2]	=	[80, 90]
80 in grades	=	True
60 in grades 	=	False
len(grades)	=	3
min(grades)	=	70
max(grades)	=	90
sum(grades) =	240

subjects = ['bio', 'cs', 'math', 'history']
len(subjects)	=	4
min(subjects)	=	'bio'
max(subjects)	=	'math'
sum(subjects)	+	TypeError  this is because the list is of strings, not int or floats


street_address = [10, 'Main Street']	Shows that int and str can exist in lists at same time.

for grade in grades:
		print(grade)
80
90
70

for item in subjects:
	print (item)

bio
cs
math
history

====================================
+++++++++++++list Methods+++++++++++

A method is a function that is inside of an object
dir(list)	would show us the methods of: append, count, extend, index, insert, pop, remove, reverse, sort.
Example:
list.append(object)		appends object to end of list
list.extend(list)		appends the list to end of list
list.pop()			removes the item at end & returns list
list.count(object)	return the number of times object occurs

colors = []
prompt = 'Enter another one of your favorite colors(return to end):'
color = input(prompt)	#this prompts user for input
	#the color entered is now the value of 'color' i.e. blue
	#so color = blue
while color != '':
	colors.append(color)
	color = input(prompt)
Enter another one of your favorite colors(return to end): brown
Enter another one of your favorite colors(return to end): red 
Enter another one of your favorite colors(return to end): 

colors	=	['blue', 'brown', 'red']
But if we forgot to add colors, we can .extend

colors.extend(['hot pink', 'green'])
colors	=	['blue', 'brown', 'red', 'hot pink', 'green']
colors.pop()	=	['blue', 'brown', 'red', 'hot pink']
colors.pop(1)	=	['blue', 'red', 'hot pink']
color.remove('red')
If we want to remove something from a list
if colors.count('yellow') > 0:
	colors.remove ('yellow')
OR
if 'yellow' in colors:
	colors.remove('yellow')

color.extend('auburn', 'taupe', 'magenta')
	This will give a TypeError because .extend needs a list
	so
color.extend(['auburn', 'taupe', 'magenta']) will work
If you want to know the index of an object
colors.index('hot pink')	=	index of where 'hot pink' is
	if 'hot pink' is not in list, prg would crash. So:
if 'hot pink' in colors:
	where = colors.index('hot pink')
	colors.pop(where)

=====================================
++++++++Mutability and Aliasing+++++++
lst = [0, 2, 4, 6, 8, 10]
lst[2] = 5	=	replaces 4 with 5

list1 = [0, 2, 4, 6, 8, 10]
list2 = list1
list1[-1] = 17	#replaces index 5 with 17
print(list1[-1]) 
print(list2[-1])

list is mutable
int, float, str, bool are NOT mutable

=====================================
+++++++++++++++range+++++++++++++++++
for num in range(10):
	print(num)
0
1
2
3
4
5
etc 

range([start,] stop[, step]) # the stop value is excluded
range(1, 10, 2)
	print(range)
1, 3, 5, 7 9

s = 15
for i in range(1, len(s)):
	print(i)
1
2
3
4
etc thru 15
for i in range(1, len(s), 2): #add step value
	print(i)
1
3
5
7
9
11
13
15


***********************************************
******************** WEEK 6 *******************
***********************************************

=============================================
++++++++++++For Loops Over Indices+++++++++++
#find adjacent repeating letters
s = 'abccdeffggh'
for i in range(len(s) - 1): #up to but not including last char
	print(i)
#this will print out 1 thru 9 on individual lines
def count_adjacent_repeats(s):
	'''(str) -> int

	Return the number of occurences of a character and an adjacent character being the same.
	>>> count_adjacent_repeats('abccdeffggh')
	3
	'''
	repeats = 0
	for i in range(len(s) - 1):
		if s[i] == s[i+1]:
			repeats = repeats + 1
	return repeats

letters = ['a', 'b', 'c', 'd']
def shift_left(L):
	''' (list) -> NoneType
	Shift each item in L one position to the left and shift the first item to the last position.
	Precondition: len(L) >= 1
	'''
	first_item = L[0]
	for i in range(1, len(L)):
		L[i - 1] = L[i]

	L[-1] = first_item # takes original L[0] & puts it to end 						 of list
	print(L)
shift_left(letters)