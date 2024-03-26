# Requirement specification
## Purpose of the application
With the help of this application, users will be able to circumvent a notoriously tiresome task: deciding what to cook.
This application supports multiple users, each of whom has their respective recipes of liking. 
## Users
Only one user role. More will be added if needed.
## Sketch of user interface
![User interface sketch](https://github.com/Germuu/ot-harjoitusty-/blob/master/documentation/Pictures/k%C3%A4ytt%C3%B6liittym%C3%A4%C3%B6.png)
## Functionalities of the basic version
### Before logging in
- The user can register into the system
  * Username must be unique and at least 4 characters
- The user can log in to the system
  * Login is successful if the username and the password are in the database.
  * If username or password is not in the database: raise an error.
### After logging in
- The user is directed to the Home menu
- The menu has two buttons :
  * My recipes directs the user to a catalog containing all previously created recipes. The My Recipes page contains a list 
   of all recipes. The user can delete a recipe with the X button. The user can also 
  click on a recipe. When a recipe is clicked, the relevant data (cooking time, ingredients, name) are displayed and can be 
  edited. A new recipe can also be created with the add button, which directs the user to a page asking for relevant data.
  * Find recipes directs the user to the search tool. The search tool allows users to fetch recipes based on the above mentioned filters, or a random recipe can be generated using the "random" button. Once filters are selected and the search button is pressed, a ranking based on number of matching criteria is displayed. When a recipe is clicked, relevant data is shown.
 ## Possible improvements
 - Shopping List: Create a feature that generates a shopping list based on the ingredients needed for selected recipes.
 - Missing ingredients : If a recipe is clicked on the ranking page after search, missing ingredients will be highlighted.
  
