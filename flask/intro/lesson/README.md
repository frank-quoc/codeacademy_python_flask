# BUILD YOUR FIRST FLASK APP

## Instructions

1. Define a third view function called ```article()``` that is bound to the URL path ```'/article'```. The function should return an ```<a>``` tag with the text ```Return back to home page``` that links to ```"/"```.
<br /><br />Run **app.py** in the terminal and navigate to http://localhost:5000/article in the browser.

2. Now, add a variable rule such that a URL whose path follows the pattern ```'/article/X'``` will trigger the ```article()``` function. Name the variable part ```article_name```.

3. Update the ```article()``` function to take a parameter called ```article_name```. Since this value is the URL slug, assume ```article_name``` will be all lower-cased with hyphens separating each word. For example, article_name could look like this:
<br />```ten-ducks-enter-local-pond```
<br />In the function body, replace the hyphens with spaces and turn the text to title-case. Then, before the ```<a>``` element in the returned HTML, add a ```<h2>``` heading containing the formatted title. Check the hint for guidance on how to make these formatting changes.
<br /><br />Try visiting various article pages such as http://localhost:5000/article/my-first-flask-app!

## [Answer](app.py)
