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

![login image](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/login.png)

The user can login by typing in a username and a password and clicking "login". 

## Register
By clicking "register" on the login page, the user can acces the registering page:

![register image](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/register.png)

If the user registers successfully, she is redirected to the login view and can use the previously created credentials

## Homepage

The homepage contains all relevant functionalities: 

![homepage](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/homepage.png)

The user can either acces their own recipes or start finding recipes.

## My recipes 
The purpose of this view is to manage recipes. If the user has recipes, they will be displayed here:

![my recipes](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/myrecipes.png)

The user can delete recipes by clicking on the X displayed on the right-hand side of the recipe name. Additionally, the user can edit recipes by clicking on their names.

## Add recipe

The user can create a recipe in the view:

![add recipe](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/addrecipe.png)

After filling in the fields, the user can create a recipe by clicking "add recipe". Ingredients must be comma-separated, and the user can input units of measure at the end of a given ingredient if needed, ex. tomatoes 2, pasta 300g, etc.

## Find recipes

when "find recipes" is clicked on the homepage, the user is directed to the following page:

![find recipes](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/findrecipes.png)

This page contains filter fields for recipes. If all/some fields are left empty, all recipes are displayed. Additionally, the user can generate a random recipe, which will be displayed under the random button. By clicking the random recipe, the user is directed to the recipe details page.

## Results
After filling in the fields on the find recipes page, and clicking the "search" button, the following view is displayed:

![results](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/searchresults.png)

Here recipes will be ranked based on matching criteria. The more ingredients match, the higher on the list the recipe will be. However, the max time filter will not display any recipes the max time of which is above the desired time.

## Recipe details

When a recipe is clicked after either generating one randomly, or searching with filters, the following page is displayed:

![Recipe details](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/recipedetails.png)

Here The user can inspect the recipe for use.














