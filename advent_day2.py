

"""
Your horizontal position and depth both start at 0. 
The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.

What do you get if you multiply your final horizontal 
position by your final depth?

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
"""
#Import document and convert to integer
a_file = open('advent_day_2.txt',"r")
#test if code works on known data from example:
coordinates = [dict.fromkeys(a_file) for data in a_file]
print(coordinates)
