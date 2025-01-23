"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### TODO
	
	# Base case - If the range is not valid, the key is not pressent
	if left > right:
		return -1

	# Calculate the middle index
	mid = (left + right) // 2

	# Check if the middle element is the key
	if mylist[mid] == key:
		return mid

	# Search the right half of the list
	elif mylist[mid] < key:
		return _binary_search(mylist, key, mid + 1, right)

	# Search the left half of the list
	else: 
		return _binary_search(mylist, key, left, mid - 1)
	
	###

def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `search_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO

	# Record the start time
	start = time.time()

	# Run the search function on the list
	search_fn(mylist, key)
	
	# Record the end time
	end = time.time()
	
	# Calculate the elapsed time and return
	return (end - start) * 1000
	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO
	# Create a list to store the results for linear time and binary time
	linear_times = []
	binary_times = []
	# Loop through the sizes list
	for size in sizes:
		# Create a list of numbers from 0 to size-1
		size = int(size)
		mylist = list(range(size))
		# Time the linear search
		linear_times.append(time_search(linear_search, mylist, -1))
		# Time the binary search
		binary_times.append(time_search(binary_search, mylist, -1))
		# Return the results as a list of tuples
	return [(size, linear_times[i], binary_times[i]) for i, size in enumerate(sizes)]
	###


def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))
# Print the results
print_results(compare_search())
