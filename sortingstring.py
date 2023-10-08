# Python Implementation


def compare(a, b):
	return ((a < b) - (a > b))


def sort_string(arr, n):
	temp = ""

	# Sort string using the bubble sort
	for i in range(n-1):
		for j in range(i+1, n):
			if compare(arr[j], arr[i]) > 0:
				temp = arr[j]
				arr[j] = arr[i]
				arr[i] = temp
	print("String in sorted order are: ")
	for i in range(n):
		print(f'Strings {i + 1} is {arr[i]}')


# Driver code
arr = ["GeeksforGeeks", "Quiz", "Practice", "Gblogs", "Coding"]
n = len(arr)
sort_string(arr, n)


# This code is contributed by Prince Kumar
