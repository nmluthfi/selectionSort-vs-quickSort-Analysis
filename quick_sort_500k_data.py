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


# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)

## IMPORANT
# Kindly, run this code locally as Google Colab as limitation
# for how much data it can proceed. Max 10 MB

#array 500,000 data

# show the array's value before it was sorted
print("500,000 Data\n")
print('Unsorted Array Data:')
print(array6_quick_sort)

# get the time before the array was shorted
before_array6 = datetime.now() 
before_sorting_time_array6 = before_array6.strftime("%H:%M:%S")
t1_array6 = datetime.strptime(before_sorting_time_array6, "%H:%M:%S")
print("Current Time Before Sorting: ", before_array6, "\n")

# do quick sort
quickSort(array6_quick_sort, 0, len(array6_quick_sort) - 1)

# show the array's value after it was sorted
print('Sorted Array in Ascending Order:')
print(array6_quick_sort)

# get the time after the array was shorted
after_array6 = datetime.now() 
after_sorting_time_array6 = after_array6.strftime("%H:%M:%S")
t2_array6 = datetime.strptime(after_sorting_time_array6, "%H:%M:%S")
print("Current Time Afer Sorting: ", after_array6)

# calculate the delta time and print it
delta_array6 = t2_array6 - t1_array6
print("\nTime needed to do sorting: ", delta_array6.total_seconds(), " second") 

print("\n")