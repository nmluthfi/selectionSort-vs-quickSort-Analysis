#importing neccessary module
import random 
from datetime import datetime, timedelta

#array7 will contain 1,000,000 data
array7_selection_sort = [] 
array7_quick_sort = []

# generate random number from -1,000,000 to 1,000,000
# then input the number into the array
for i in range(1000000):
  array7_selection_sort.append(random.randint(-1000000, 1000000))
  array7_quick_sort.append(random.randint(-1000000, 1000000))


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


# array 1,000,000 data

# show the array's value before it was sorted
print("1,000,000 Data\n")
print('Unsorted Array:')
print(array7_selection_sort)

# get the time before the array was shorted
before_array7 = datetime.now()
before_sorting_time_array7 = before_array7.strftime("%H:%M:%S")
t1_array7 = datetime.strptime(before_sorting_time_array7, "%H:%M:%S")
print("Current Time Before Sorting: ", before_array7, "\n")

# do selection sort
selectionSort(array7_selection_sort, len(array7_selection_sort))

# show the array's value after it was sorted
print('Sorted Array Data in Ascending Order:')
print(array7_selection_sort)

# get the time after the array was shorted
after_array7 = datetime.now()
after_sorting_time_array7 = after_array7.strftime("%H:%M:%S")
t2_array7 = datetime.strptime(after_sorting_time_array7, "%H:%M:%S")
print("Current Time Afer Sorting: ", after_array7)

# calculate the delta time and print it
delta_array7 = t2_array7 - t1_array7
print("\nTime needed to do sorting: ", delta_array7.total_seconds(), " second") 

print("\n")