# LEARN PYTHON: INHERITANCE AND POLYMORPHISM

1. Create a class ```SortedList``` that inherits from the built-in type ```list```.

2. Recall that lists have a ```.append()``` method that takes a two arguments, ```self and value```. We’re going to have ```SortedList``` perform a sort after every ```.append()```.
<br /><br />Overwrite the ```append``` method, leave it blank for now with the ```pass``` keyword.

3. First, we want our new ```.append()``` to actually add the item to the list.
<br /><br />Write the code that would get ```SortedList``` to behave like a normal ```list``` when calling the ```.append()``` method.

4. After you’ve appended the new value, sort the list.

5. Incredible! We subclassed a Python primitive and introduced new behavior to it.
<br /><br />Some things to consider:
<br /><br />When a ```SortedList``` gets initialized with unsorted values (say if you call ```SortedList([4, 1, 5])```) those values don’t get sorted! How would you change ```SortedList``` so that the list is sorted right after the object gets created?
<br />What other Python builtins have functionality “missing”? Could you write a new dictionary that uses a fallback value when it tries to retrieve an item and can’t?

## [Answer](answer.py)
