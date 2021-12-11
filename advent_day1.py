"""
Find the full description (including download of datasheet) on:
https://adventofcode.com/2021/day/1
"""

#Import document and convert to integer
a_file = open('advent_day_one.txt',"r")
#test if code works on known data from example:
#a_file = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263 ]
sweep_list = [int(data) for data in a_file]
start_number = sweep_list[0]

#the actual code:
"""
How many measurements from a_file are larger than the previous measurement?
"""
counter = 0
decrease_counter = 0
#remember, the length of the list is 2000, the last index is 1999
while counter < len(sweep_list)-1:
	#if the item is smaller than the next item.
    if sweep_list[counter] > sweep_list[counter+1]: 
        print("decrease")
   # else:
    #    print("increase")
        if 'decrease':
        	decrease_counter += 1
    counter += 1 #add one to counter and re-assign

#Test if all variables are taken in to account (should be 2000): 
print(f"Test total: {(counter) +1}") 
#test if code counts decrease
print(f"Test decrease: {decrease_counter}")
#Final awnser:
print(f"Total increases: {(counter)-(decrease_counter)}")


