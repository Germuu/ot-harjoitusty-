# Manual

Download the source code of the latest release by selecting *Source code* from under *Assets*.

## Configuration

The database used can be customized using the .env file located in the main directory.

The contents of the .env file are:
```bash
DATABASE_FILENAME=database.sqlite
```
## Launching
Dependencies are installed with:
```bash
poetry install
```

The database is initialized with:
```bash
poetry run invoke init-database
```

The application can now be started with:
```bash
poetry run invoke start
```

## Login
The login view is displayed when the application is started:

![Login Image](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/login.png)

Users can log in by entering a username and password and clicking "login".

## Register
By clicking "register" on the login page, users can access the registration page:

![Register Image](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/register.png)

Successful registration redirects users to the login view, where they can use the newly created credentials.

## Homepage
The homepage consolidates all relevant functionalities:

![Homepage](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/homepage.png)

Users can access their own recipes or start searching for recipes.

## My Recipes
This view allows users to manage their recipes. If users have saved recipes, they will be displayed here:

![My Recipes](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/myrecipes.png)

Users can delete recipes by clicking the X icon next to the recipe name. Additionally, they can edit recipes by clicking on their names.

## Add Recipe
Users can create a new recipe in this view:

![Add Recipe](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/addrecipe.png)

After filling in the fields, users can create a recipe by clicking "add recipe". Ingredients must be comma-separated, and users can specify units of measure if needed (e.g., tomatoes 2, pasta 300g, etc.).

## Find Recipes
Clicking "find recipes" on the homepage directs users to the following page:

![Find Recipes](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/findrecipes.png)

This page contains filter fields for recipes. Leaving all fields empty will display all recipes. Alternatively leaving some fields empty widens the range of filtering. Users can also generate a random recipe, which will be displayed under the random button. Clicking on the random recipe redirects users to the recipe details page.

## Results
After filling in the fields on the find recipes page and clicking the "search" button, users see the following view:

![Results](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/searchresults.png)

Recipes are ranked based on matching criteria. The more ingredients match, the higher the recipe is on the list. However, the max time filter will not display recipes with a time exceeding the desired limit.

## Recipe Details
When a recipe is clicked after either generating one randomly or searching with filters, users are directed to the following page:

![Recipe Details](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/recipedetails.png)

Here, users can inspect the recipe for further details.















