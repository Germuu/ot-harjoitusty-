# Requirement Specification

## Purpose of the Application

This application aims to simplify the often tedious task of deciding what to cook. Users can create and manage their own recipe collections, making meal planning more efficient and enjoyable.

## Users

The application currently supports a single-user role, with the flexibility to add more roles as necessary in the future.

## Sketch of User Interface

![User Interface Sketch](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/k%C3%A4ytt%C3%B6liittym%C3%A4%C3%B6.png)

## Functionalities of the Basic Version

### Before Logging In

- **User Registration**:
  - Users can register with the system. &#10004;
  - Usernames must be unique and at least 4 characters long.
  
- **User Login**:
  - Users can log in to the system. &#10004;
  - Login is successful if the username and password match those in the database. &#10004;
  - If the username or password is not found in the database, an error is raised. &#10004;

### After Logging In

- **Home Menu**:
  - Upon logging in, users are directed to the Home menu. &#10004;
  - The Home menu includes two buttons:
    * **My Recipes**: Takes users to a catalog of their previously created recipes. &#10004;
      - Users can delete recipes using the X button. &#10004;
      - Clicking on a recipe displays its relevant data (cooking time, ingredients, name) for editing. &#10004;
      - Users can also create new recipes using the add button, which prompts them for relevant data. &#10004;
    * **Find Recipes**: Directs users to the search tool. &#10004;
      - The search tool allows users to filter recipes based on various criteria. &#10004;
      - Users can generate a random recipe using the "random" button. &#10004;
      - After applying filters and clicking the search button, recipes are ranked based on matching criteria. &#10004;
      - Clicking on a recipe displays its relevant data. &#10004;

## Further Improvements
- **Missing Ingredients**:
  - Highlight missing ingredients when a recipe is clicked from the search ranking page.

- **Shopping List**:
  - Implement a feature to generate a shopping list based on the ingredients needed for selected recipes.
  


  
