

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

=============================================
+++++++++++Parallel Lists & Strings++++++++++

def sum_items(list1, list2):
	'''(list of number, list of number) -> list of number
	
	Return a new list in which each item is the sum of the items at the corresponding postition of list1 and list2.

	Precondition: len(list1) == len(list2)
	
	>>> sum_items([1, 2, 3], [2, 4, 2])
	[3, 6, 5]
	>>> sum_items([1, 2], [2, 4, 2])
	[3, 6]  #1st list only has 2 indexes, so it will never see 3rd on list2
	>>> sum_items([2, 4, 2], [1, 2])
	This will raise an IndexError because there is no index of 2 on 2nd list
	''' 

	sum_list = []
	for i in range(len(list1)):
		sum_list.append(list1[i] + list2[i])
	return sum_list

def count_matches(s1, s2):
	''' (str, str) -> int

	Return the nubmer of positions in s1 that contain the same character at the corresponding position of s2.

	Precondition: len(s1) == len(s2)

	>>> count_matches('ate', ape')
	2
	>>> count_matches('head', 'hard')
	2
	'''

	num_matches = 0
	for i in range(len(s1)):
		if s1[i] == s2[i]:
			num_matches + 1
	return num_matches


=============================================
+++++++++++++++++Nested Lists++++++++++++++++

grades = [['Assignment 1', 80], ['Assignment 2', 90], ['Assignment 3', 70]]
len(grades)
3
grades[0]
	['Assignment 1', 80]
grades[1]
	['Assignment 2', 90]
len(grade[0])
	2

Can do this with a "for" loop as well
for item in grades:
	print(item)
['Assignment 1', 80]
['Assignment 2', 90]
['Assignment 3', 70]

Can use multiple indexes to get specific Values
grades[0][0]
	'Assignment 1'
grades[0][1]
	80

A function to calculate the average grade
def calculate_average(asn_grades);
	''' (list of list of [str, number]) -> float

	Return the average of grades in asn_grades.

	>>> calculate_average([['A1, 80'], ['A2', 90]])
	85.0
	'''

	total = 0
	for item in asn_grades:
		total = total + item[1]
	return total / len(asn_grades)

numbers = [[1, 2], 3, [4, 5]]
len(numbers)
	3   #because each sublist is treated as a single element. Thus 2 lists and 1 int = 3.

numbers[2][0] 	=	4
numbers[1]		=	3
numbers[0][1]	=	2

=============================================
+++++++++++++++++Nested Loops++++++++++++++++

for i in range(10, 13):
	for j in range(1, 5):
		print(i, j)

10 1
10 2
10 3
10 4
11 1
11 2
11 3
etc. thru 12 4

grades = [[70, 75, 80],[70, 80, 90, 100],[80, 100]]
english = grades[0] # this sets the first list to 'english'
english				# this returns the value of the variable 'english'
	[70, 75, 80]

total = 0			# this loop would give the average grade of 'english'
for mark in english:
	total = total + mark
	return total / len(english)

def averages(grades):
	''' (list of list of number) -> list of float
	
	Return a new list in which each item is the average of the grades in the inner list at the corresponding potition of grades.

	>>> averages([[70, 75, 80],[70, 80, 90, 100],[80, 100]])
	[75.0, 85.0, 90.0]
	'''
	averages = []
	for grades_list in grades:
		#calculate the average of grades and apped it to averages
		total = 0
		for i in grades_list:
			total = total + i

		averages.append(total / len(grades_list))

	return averages


=============================================
++++++++++++++++Reading Files++++++++++++++++
To open a file to read:
open(filename, mode)
	modes: 	'r' - open to read
			'w' - open for writing (will delete any previous data)
			'a' - open to append
When opening a file, the full path must be given. So its best to assign a variable
filename = '/home/david/Documents/filename.txt'
open_file = open(filename, 'r')

Once a file is open for reading, we can use the READLINE method
open_file.readline() # will read 1 line of the file and return it 1 at a time

This lets us use a 'while' loop to read each line automatically.
open_file = open(filename.txt, 'r')
line = open_file.readline()
while line != '':
	print(line, end='') # prints line, end='' removes extra <CR>
	line = open_file.readline() # moves to next line in file & goes to top of loop

To close the file, you MUST close the file.
	open_file.close()

If we want to only get the first stanza/paragraph we can
filename = '/home/david/Documents/filename.txt'
open_file = open(filename, 'r')
line = open_file.readline()
while line != '\n':	# prints each line til it finds one that only has \n
	print(line, end='')
	line = open_file.readline()

If we want to read every line in a file, a "for" loop is easy.
filename = '/home/david/Documents/filename.txt'
open_file = open(filename, 'r')
for line in open_file:
	print(line, end='')

Or if the file isnt large, can read it in a method call. This method reads the entire file & returns it as a single string including \n character.
print(open_file.read())


Can also use a readlines method, which returns a list of all the lines in the file. This way is useful as then we can use it to get an index of a specific line  	lines[0] or lines[4] etc.

open_file.readlines()  # NOT the same as readline!!
Like this:
	open_file = open(filename, 'r')
	lines = open_file.readlines()
	for line in lines:
		print(lines, end='')

open_file.close()

=============================================
++++++++++++++++Writing Files++++++++++++++++
open(filename, mode)
the WRITE method is like print but does not append an extra newline character

import tkinter.filedialog
from_filename = tkinter.filedialog.askopenfilename() #prompts user for filename
to_filename = tkinter.filedialog.asksaveasfilename() #prompts user for save filenam

from_file = open(from_filename, 'r')
contents = from_file.read()
from_file.close()

to_file = open(to_filename, 'w')
to_file.write('Copy\n') #we have to add the newline as .write does not do it
	5
to_file.write(contents)
	540
to_file.close()

=================================================
++++++++++++++++Develop a Program++++++++++++++++



***********************************************
******************* WEEK 7 ********************
***********************************************

=============================================
++++++++++++++++++++Tuples+++++++++++++++++++
Lists are mutable sequences. Lists use square brackets.
Tuples are immutible sequences. Tuples use parenthesis.

Tuple are Like
	tup = ('a', 3, 0.2) is like a list of list=['a', 3, 0.2]
You can index Tuples
tup[0]	=	'a'
tup[1]	=	3
tup[2]	=	0.2
tup[-1]	=	0.2
You can slice Tuples, which return a Tuple
tup[:2]	=	('a', 3)
tup[1:3]	(3, 0.2)
Tuples only have count, and index methods.
You can iterate of items in a Tuples
	for item in tup:
		print(item)
a
3
0.2

len(tup)
3

for i in range(len(tup)):
	print(tup[i])
a
3
0.2

=============================================
++++++++++++++++++Type dict++++++++++++++++++
grades = [['A1', 80], ['A2', 70], ['A3', 90]] #a nested list
grades = [0]
	['A1', 80]
grades[1][0]
	'A2'

dict (dictionary) uses key:value pairs. Keys MUST be unique.
asn_to_grade = {'A1': 80, 'A2': 70, 'A3':90}
asn_to_grade['A2']
	70
'A4' in asn_to_grade
	False
'A2' in asn_to_grade
	True
80 in asn_to_grade
	False (80 is not a key, it is a value)

Add a key:value pairs
asn_to_grade['A4'] = 85
len(asn_to_grade)
	4
asn_to_grade['A4'] = 90 (this changes the value of A4)
	
del asn_to_grade['A4']
len(asn_to_grade)
	3

for assignment in asn_to_grade:
	print(assignment)
A1
A3
A2


for assignment in asn_to_grade:
	print(asn_to_grade[assignment])
80
90
70

for assignment in asn_to_grade:
	print(assignment, asn_to_grade[assignment])
A1 80
A3 90
A2 70

A dictionary can be empty
d = {}
len(d)
	0
d = {'a': 2, 5 : 8} #can use str or int, etc
dictionary are mutable
dictionary is unordered

Keys are immutable

d[[1, 2]] = 'banana' will result in a TypeError
d[(1, 2)] = 'banana' is acceptable because it is a tuple and tuples are immutable


=============================================
+++++++++++++++Inverting a dict++++++++++++++
Create a dictionary as such
fruit_to_color = {
	'banana': 'yellow',
	'cherry': 'red',
	'orange': 'orange',
	'pear': 'green',
	'peach': 'orange',
	'plug': 'purple',
	'pomegranate': 'red',
	'strawberry': 'red'}

Dictionaries are not ordered
fruit_to_color['banana']	=	'yellow'
fruit_to_color['orange']	=	'orange'

for fruit in fruit_to_color:
	print(fruit, fruit_to_color[fruit])

pomegranate red
strawberry red
peach orange
cherry red
etc

#Invert fruit_to_color
color_to_fruit = {}
for fruit to fruit_to_color:
	color = fruit_to_color[fruit]
	# if color is not already a key in the accumulator, add color: [fruit] as an entry
	if not (color in color_to_fruit):
		color_to_fruit[color] = [fruit]
 	# otherwise, append fruit to the existing list
 	else:
 		color_to_fruit[color].append(fruit)
#	color_to_fruit[color] = fruit

color_to_fruit['orange']	=	['peach', 'orange']
color_to_fruit['orange']['1']	=	'orange'
color_to_fruit['red']		=	['pomegranate', 'strawberry', 'cherry']
color_to_fruit['red'][-1]	=	'cherry'

=============================================
+++++++++++++++Populating a dict++++++++++++++
Read from a file and store it into a dictionary


gradefile = open('/home/david/text_filename_here.txt')
def read_grades(gradefiles):
	''' (file open for reading) -> dict of {float: list of str}

	Read the grades from gradefile and return a dictionary where each key is a grade and each value is the list of the ids of students who earned that grade.

	Precondition: grade file starts with a header that contains no blank lines, then has a blank line, and then lines containing a student number and a grade.

	'''

	# skip over the header
	line = gradefile.readline()
	while line != '\n':
		line = gradefile.readline()

	# read the grades from file, accumulate them into dict.
	grade_to_ids = {}
	line = gradefile.readline()

	while line != '':

		student_id = line[:4]
		grade = float(line[4:].strip())

		if grade not in grade_to_ids:
			grade_to_ids[grade] = [student_id]
		else:
			grade_to_ids[grade].append(student_id)

		line = gradefile.readline()
	return grade_to_ids

	call the function to run it
	read_grades(gradesfile)