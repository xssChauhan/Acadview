'''
1. There is a list [1,2,3,4,5]. Now ,I want to extract the 2nd,3rd and 4th element from the list and store it into another list.
'''

def solution1():
	a = range(1,6)
	return a[1:4]


'''
Write a program to find the last element of the list WITHOUT using len() function
'''
def solution2():
	a = range(1,6)
	return a[-1]


print solution1()
print solution2()