"""
Here follows part two of the advent of code day one. 
"""

#Import document and convert to integer
a_file = open('advent_day_one.txt',"r")
#test if code works on known data from example:
#a_file = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263 ]
sweep_list = [int(data) for data in a_file]

"""
The actual coding:
count the number of times the sum of measurements in this sliding window increases
"""

#variables
window = 3
new_sweep_list = []
counter = 0
increase_counter = 0
decrease_counter = 0
none_counter = 0

"""
Sweeplist is seperated in pairings of 3 and 
hops to the next (+1) number, to do it again.
Then new_sweep_list is created by the sum of the outcome. 
and appended to the new variable new_sweep_list.
"""
for grouping in range(len(sweep_list) - window + 1):
    #print(sweep_list[grouping: grouping + window])
    new_sweep_list.append(sum((sweep_list[grouping: grouping + window])))
    print(new_sweep_list)


#while counter less than lenght of new_sweeplist (-1, so it ends in time).    
while counter < len(new_sweep_list) -1:
    """Assign counter values to increase and decrease counter."""
    #If list bigger than next in list.
    if new_sweep_list[counter] > new_sweep_list[counter+1]:
        counter += 1
        decrease_counter += 1
    #if list smaller than next in list.
    if new_sweep_list[counter] < new_sweep_list[counter+1]:
        counter += 1
        increase_counter += 1   
    #if list is same as next in list.
    else: 
        none_counter += 1
        counter += 1
        

#test if the code comes trough and see answer.
#counter +1 because the first outcome isn't considered in the while loop. 
print(f"{new_sweep_list} \n\ntotal: {counter+1} \nincrease: {increase_counter} "
f"\ndecrease: {decrease_counter} \nno changes: {none_counter}")



