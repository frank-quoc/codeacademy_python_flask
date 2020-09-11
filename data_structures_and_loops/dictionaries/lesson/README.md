# CREATING DICTIONARIES

1. We are building a music streaming service. We have provided two lists, representing songs in a user’s library and the amount of times each song has been played.
<br /><br />Using a list comprehension, create a dictionary called ```plays``` that goes through ```zip(songs, playcounts)``` and creates a ```song:playcount``` pair for each ```song in songs``` and each ```playcount in playcounts```.

2. Print ```plays```.

3. After printing ```plays```, add a new entry to it. The entry should be for the song ```"Purple Haze"``` and the playcount is ```1```.

4. This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for ```"Respect"``` to be 94 in the ```plays``` dictionary.

5. Create a dictionary called ```library``` that has two key: value pairs:
  * key ```"The Best Songs"``` with a value of ```plays```, the dictionary you created
  * key ```"Sunday Feelings"``` with a value of an empty dictionary

6. Print ```library```.

## [Answer](answer.py)
