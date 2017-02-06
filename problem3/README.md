1)	Given an array of N integers and a number l, perform l left rotations on the array then print the array.
	A left rotation operation on an array shifts each of the array's elements 1 unit to the left.
	example: array {1, 2, 3, 4} after 2 left shifts would become {3, 4, 1, 2}

	Input format
	1st line contains two space-separated integers denoting the respective values of N (the number of integers) and l (the number of left rotations you must perform). 
	2nd line contains N space-separated integers describing the respective elements of the array's initial state.

	Output/Print a single line of N space-separated integers denoting the final state of the array after performing  left rotations.
	
2)	Given N integers , count the total pairs of integers that have a difference of K
	
	Input Format
	1st line contains two space-separated integers denoting the respective values of N (the number of integers) and K (the diffenrence)
	2nd line contains N space-separated integers. All the N numbers are distinct.
	
	Output/Print the number of pairs having difference equal to K
	example:
	Input:  6 4
			8 12 16 4 0 20
	Output: 5
	There are 5 pairs with difference 4, the pairs are 
	{0, 4}, {4, 8}, {8, 12}, {12, 16} and {16, 20} 
	//It can be done either by brute force (running 2 loops and finding all possible pairs) or by sorting the input and binary searching