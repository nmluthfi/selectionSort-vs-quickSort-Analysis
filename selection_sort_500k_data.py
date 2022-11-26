#importing neccessary module
import random 
from datetime import datetime, timedelta

#array6 will contain 500,000 data
array6_selection_sort = [] 
array6_quick_sort = []

# generate random number from -500,000 to 500,000
# then input the number into the array
for i in range(500000):
  array6_selection_sort.append(random.randint(-500000, 500000))
  array6_quick_sort.append(random.randint(-500000, 500000))


# Selection sort in Python
def selectionSort(array, size):
   
    # we'll iterate for the size of the array
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


#array 500,000 data

# show the array's value before it was sorted
print("500,000 Data\n")
print('Unsorted Array:')
print(array6_selection_sort)

# get the time before the array was shorted
before_array6 = datetime.now() 
before_sorting_time_array6 = before_array6.strftime("%H:%M:%S")
t1_array6 = datetime.strptime(before_sorting_time_array6, "%H:%M:%S")
print("Current Time Before Sorting: ", before_array6, "\n")

# do selection sort
selectionSort(array6_selection_sort, len(array6_selection_sort))

# show the array's value after it was sorted
print('Sorted Array Data in Ascending Order:')
print(array6_selection_sort)

# get the time after the array was shorted
after_array6 = datetime.now() 
after_sorting_time_array6 = after_array6.strftime("%H:%M:%S")
t2_array6 = datetime.strptime(after_sorting_time_array6, "%H:%M:%S")
print("Current Time Afer Sorting: ", after_array6)

# calculate the delta time and print it
delta_array6 = t2_array6 - t1_array6
print("\nTime needed to do sorting: ", delta_array6.total_seconds(), " second") 

print("\n")