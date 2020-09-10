# Advanced Python Code Challenges: Lists

## 1. Every Three Numbers
Create a function called ```every_three_nums``` that has one parameter named ```start```.
<br /><br />The function should return a list of every third number between ```start and 100``` (inclusive). For example, ```every_three_nums(91)``` should return the list ```[91, 94, 97, 100]```. If ```start``` is greater than ```100```, the function should return an empty list.

## 2. Remove Middle
Create a function named ```remove_middle``` which has three parameters named ```lst, start, and end```.
<br /><br />The function should return a list where all elements in ```lst``` with an index between ```start and end``` (inclusive) have been removed.
<br /><br />For example, the following code should return ```[4, 23, 42]``` because elements at indices ```1, 2, and 3``` have been removed:
<br /><br />```remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)```

## 3. More Frequent Item
Create a function named ```more_frequent_item``` that has three parameters named ```lst, item1, and item2```.
<br /><br />Return either ```item1 or item2``` depending on which item appears more often in ```lst```.
<br /><br />If the two items appear the same number of times, return ```item1```.

## 4. Double Index
Create a function named ```double_index``` that has two parameters: a list named ```lst``` and a single number named ```index```.
<br /><br />The function should return a new list where all elements are the same as in ```lst``` except for the element at ```index```. The element at ```index``` should be double the value of the element at ```index``` of the original ```lst```.
<br /><br />If ```index``` is not a valid index, the function should return the original list.
<br /><br />For example, the following code should return ```[1,2,6,4]``` because the element at index 2 has been doubled:
<br /><br />```double_index([1, 2, 3, 4], 2)```
<br /><br />After writing your function, un-comment the call to the function that we’ve provided for you to test your results.

## 5. Middle Item
Create a function called ```middle_element``` that has one parameter named ```lst```.
<br /><br />If there are an odd number of elements in ```lst```, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.
