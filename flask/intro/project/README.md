# Adopt a Pet

Imagine you are looking to add a new furry friend to your family! On the pet adoption website, you browse through the categories of animals and select the one you’re interested in, which brings you to another page that contains a list of available pets. Then, you continue your search by further clicking on an individual pet to view its profile page.

Every time you navigate to a different webpage, your browser is making a request to the web server. Thanks to routing, the server knows exactly which endpoint should handle the request and can return the correct HTML page to display.

In this project, you’ll use Python’s Flask framework to create a simple pet adoption site that contains multiple routes.

Let’s get started!

## Set up the Flask app
1. At the top of app.py, import the Flask class from the flask module.

2. Create an instance of the Flask class, passing in __name__, and save the object to a variable called app.
<br /><br />If you run your code now, you will see a URL not found error, but we will fix that in the next step when you create your first route!

3. To create the index route, first define a function called index() that returns an HTML ```<h1>``` element with the text Adopt a Pet!. Remember that HTML can be returned as a string.

4. Use the route() decorator to bind the URL path '/' to the index() function.
<br /><br />Run your code now and you should see the heading displayed on the page!

5. Let’s add some more elements to the page. Right after the ```<h1>``` element, add a ```<p>``` element that contains the text Browse through the links below to find your new furry friend:.

6. Now after the <p> element, create an unordered list using ```<ul>```. The bulleted list should contain three items: Dogs, Cats, and Rabbits. Remember to use ```<li>``` to create each item.

## Create the animals route
7. The site is looking good so far! The next step is to create individual pages for each animal type and link them in the bulleted list. To do that, we’ll add a new animals route.
<br /><br />First, define a function called animals(). In the function body, create a string containing an ```<h1>``` element with the text List of pets, and assign it to the variable html. Return html from the function.

8. Use the route() decorator to associate the animals() function with the URL pattern '/animals/X', where X is a variable section of the URL. Name the variable part pet_type.

9. Next, update the animals() function to take a parameter called pet_type. In the function body, modify the ```<h1>``` heading to read List of X, where X is pet_type.

10. We’re ready to create links on the index page that links to each individual animal page! Inside the index() function, turn each bulleted list item into a link by adding an <a> element within each <li> element:
  * Dogs should link to '/animals/dogs'
  * Cats should link to '/animals/cats'
  * Rabbits should link to '/animals/rabbits'
Now run your code and try clicking on the links!

## Populate page content
11. Using the file navigator near the top left corner of the code editor, open up helper.py. This file contains a dictionary named pets that contains some data that we can use to populate the webpages.
<br /><br />The pets dictionary contains three elements, one for each animal type. The key is the animal type and the value is a list of dictionaries, each of which contains info about an individual pet.
<br /><br />Start by importing the pets dictionary at the top of app.py.

12. Inside the animals() function, you’ll be modifying html to display the names of all available pets that are of pet_type.
<br /><br />Right before the return statement, create a for loop that iterates over each element in the list of pets. You can access the appropriate list of pets in the pets dictionary by the key, pet_type. Inside the loop, create a <li> element for each pet’s name and concatenate the string to html.
<br /><br />Then, make sure to concatenate the opening <ul> tag to html before the loop and the closing </ul> tag after the loop, such that the <li> elements would be nested inside the <ul> element.
<br /><br />If you run your code and navigate to each animal page, you can see a bulleted list of available pets!

## Create the pet route
13. The next step is to create and link to individual profile pages for each pet. To do that, we’ll add a new pet route.
<br /><br />Define a function called pet() that is associated with the URL pattern '/animals/X/#', where X and # are variable sections of the URL. The section indicated by X should be called pet_type and the section indicated by # should be called pet_id. Use a converter to specify that pet_id must be a positive integer.
<br /><br />Then, pass pet_type and pet_id to the pet() function.

14. In the function body, create a variable called pet that stores the profile information of the pet who is of pet_type and has index position pet_id in its list of pets.
<br /><br />In other words, first access the appropriate list of pets in the pets dictionary by the key, pet_type. Then, access the appropriate dictionary in the list of pets by the index position, pet_id.
<br /><br />Your resulting pet dictionary will look like this:
```
{
  'name': ...,
  'age': ...,
  'breed': ...,
  'description': ...,
  'url': ...
}
```

15. Return an HTML ```<h1>``` element containing the pet’s name from the pet() function. You can access the pet’s name from the pet dictionary you created in the previous step.

16. Now, we’re ready to create links on the animal page that links to each individual pet profile page! Inside the animals() function, turn each bulleted list item into a link by adding an ```<a>``` element within each ```<li>``` element.
<br /><br />The URL we want to link to should follow the pattern '/animals/X/#', where X is pet_type and # is the index position. In order to get the latter, we must modify the for loop by using enumerate() to simultaneously loop over indices.
<br /><br />Once you’re done, run your code and try navigating to an individual pet’s profile page.

17. Finally, let’s add some more content to the profile page! Inside the pet() function, right after the ```<h1>``` element, add the following elements to display the profile info stored in the pet dictionary:
  * ```<img>``` to display the photo at the given URL
  * ```<p>``` that contains the pet’s description
  * ```<ul>``` with two ```<li>``` for the pet’s breed and age
  
 ## [Project](app.py)
