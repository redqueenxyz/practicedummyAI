## tutorialAI
### Problem 3

To complete this problem, you may use one of the languages approved for this project, i.e. Python, Javascript, or C to solve the following problems. 

Code submissions should take the form of a pull request with the solution code in this subdirectory (i.e. `problem3/solution.py`). Could should be fully documented, account for errors, and oeprate effeciently. 

1)	Define a function `rotate` that takes an array `l` of N integers and a number `j`, perform `j` left rotations on the array then print the array. A left rotation operation on an array shifts each of the array's elements 1 unit to the left.
	
	#### Example: 
	Array `{1, 2, 3, 4}` after 2 left shifts would become `{3, 4, 1, 2}`.

	#### Tests: 
	Input:
	```
	rotate({1,2,3,4}, 2)
	rotate({1,2,3,4,5,6,7,8,9}, 4)
	```
	Output:
	```
	{3,4,1,2}
	{6,7,8,9,1,2,3,4,5}
	```
	
2)	Define a function `findPairswithDiff` that takes an array `J` of N integers and some difference `k`, and returns an array of integer pairs that have that difference `k`. 
	
	#### Example: 
	Array `{8 12 16 4 0 20}` has 5 pairs with difference 4: `{0, 4}, {4, 8}, {8, 12}, {12, 16} and {16, 20}`.

	#### Tests: 
	Input:
	
	```
	findPairswithDiff([8, 12, 16, 17, 4, 0, 20], 4)
	findPairswithDiff([1,23,45,5,6,7,99,1,2,3,55,2],2)
	```
	
	Output:
	```
	[(4, 0), (8, 4), (12, 8), (16, 12)]
	[(5, 3)]
	```
	
