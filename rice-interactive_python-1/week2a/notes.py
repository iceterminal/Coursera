# Event driven programming.

# START program -> INITIALIZE program -> WAIT
	#	program waits for some 'event' then goes off and runs a handler
	#	Eventually an event will occur to call the program to quit. Then program ends.

# What are events? There are very many type. For this class we'll focus on 4.
#	1. Input events: button, text box, 
#	2. Keyboard events: key down, key up
#	3. Mouse events: click, drag, scroll
#	4. Timer events: based on Timer

# Event queue
#	Happens internally and the system puts them into the queue.
#	Events happen one at a time. If one event is in process, the next event is placed into the queue like FIFO


# Variables: Local vs Global
#	Variables created inside of functions are called "Local Variables"
#	Variables created outside of functions are called "Global Variables"
#		Global variables are available inside of functions. Local vars are ONLY available inside of functions
#		You can get a local var to modify the global var by using 'global' in front"
			def function():
				global varname
#				
