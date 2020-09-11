# CODE CHALLENGE: LOOPS

## Divisible by Ten
Create a function named ```divisible_by_ten()``` that takes a list of numbers named ```nums``` as a parameter.
<br /><br />Return the count of how many numbers in the list are divisible by ```10```.

## Greetings
Create a function named ```add_greetings()``` which takes a list of strings named ```names``` as a parameter.
<br /><br />In the function, create an empty list that will contain each greeting. Add the string ```"Hello, "``` in front of each name in ```names``` and ```append``` the greeting to the list.
<br /><br />Return the new list containing the greetings.

## Delete Starting Even Numbers
Write a function called ```delete_starting_evens()``` that has a parameter named ```lst```.
<br /><br />The function should remove elements from the front of ```lst``` until the front of the list is not even. The function should then return ```lst```.
<br /><br />For example if ```lst``` started as ```[4, 8, 10, 11, 12, 15]```, then ```delete_starting_evens(lst)``` should return ```[11, 12, 15]```.
<br /><br />Make sure your function works even if every element in the list is even!

## Odd Indices
Create a function named ```odd_indices()``` that has one parameter named ```lst```.
<br /><br />The function should create a new empty list and add every element from ```lst``` that has an odd index. The function should then return this new list.
<br /><br />For example, ```odd_indices([4, 3, 7, 10, 11, -2])``` should return the list ```[3, 10, -2]```.

## Exponents
Create a function named ```exponents()``` that takes two lists as parameters named ```bases and powers```. Return a new list containing every number in bases ```raised``` to every number in ```powers```.
<br /><br />For example, consider the following code.
<br /><br />```exponents([2, 3, 4], [1, 2, 3])```
<br /><br />the result would be the list ```[2, 4, 8, 3, 9, 27, 4, 16, 64]```. It would first add two to the first. Then two to the second. Then two to the third, and so on.

## Larger Sum
Create a function named ```larger_sum()``` that takes two lists of numbers as parameters named ```lst1 and lst2```.
<br /><br />The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return ```lst1```.

## Over 9000
Create a function named ```over_nine_thousand()``` that takes a list of numbers named ```lst``` as a parameter.
<br /><br />The function should sum the elements of the list until the sum is greater than ```9000```. When this happens, the function should return the sum. If the sum of all of the elements is never greater than ```9000```, the function should return total sum of all the elements. If the list is empty, the function should return ```0```.
<br /><br />For example, if ```lst``` was ```[8000, 900, 120, 5000]```, then the function should return ```9020```.

## Max Num
Create a function named ```max_num()``` that takes a list of numbers named ```nums``` as a parameter.
<br /><br />The function should return the largest number in ```nums```

## Same Values
Write a function named ```same_values()``` that takes two lists of numbers of equal size as parameters.
<br /><br />The function should return a list of the indices where the values were equal in ```lst1 and lst2```.
<br /><br />For example, the following code should return ```[0, 2, 3]```
<br /><br />```same_values[5, 1, -10, 3, 3], [5, 10, -10, 3, 5])```

## Reversed List
Create a function named ```reversed_list()``` that takes two lists of the same size as parameters named ```lst1 and lst2```.
<br /><br />The function should return ```True``` if ```lst1``` is the same as ```lst2``` reversed. The function should return ```False``` otherwise.
<br /><br />For example, ```reversed_list([1, 2, 3], [3, 2, 1])``` should return ```True```.
