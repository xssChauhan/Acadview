'''
 There are Two lists 
 A = [1,2,3,4,5]
 B = [6,7,8,9,10]
 Write a program to make one single list out of the two. So the result looks like:
	C = [1,2,3,4,5,6,7,8,9,10]
'''

def solution1():
	a = range(1,6)
	b = range(6,11)
	return a + b

'''
There’s a dictionary:
A = { 1:1 ,2:2 ,3:3 ,4:4 , 5:5 }
Write a program to convert the dictionary into a list such that the entry each key-value 
	Pair occurs as a list. so 1:1 is made into [1,1]
	So the result should look like this:
		[ [1,1] , [2,2] ,[3,3] , [4,4] , [5,5] ]
'''

def solution2():
	a = { 1:1 , 2:2 , 3:3 , 4:4 ,5:5}
	return [[i,e] for i,e in a.iteritems()]

'''
There are two dictionaries : 
A =  {  1:1 , 2:2 , 3:3 , 4:4 , 5:5}
B = {6:6 , 7:7 , 8:8 ,9:9 , 10 : 10}
Write a program to merge these two dictionaries. The result should look like this:
C = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
'''

def solution3():
	a = { e:e for e in range(1,6) }
	b = { e:e for e in range(6,11) }
	c = {}
	c.update(a)
	c.update(b)
	return c



print solution1()
print solution2()
print solution3()