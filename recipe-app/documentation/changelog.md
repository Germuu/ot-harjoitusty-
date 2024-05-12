
# Changelog

## [Week 3]

### Added
- Implemented user registration functionality.
- Implemented user login functionality.
- Integrated user management features with the UI.
- Created database tables for users and recipes.
- Implemented service layer for user management.
- Added UserRepository class to manage user information.
- Added RecipeRepository class to manage recipe data.
- Created a test to ensure the correct functionality of adding users.

### Changed
- Refactored repository classes to handle user-related operations.
- Updated UI to support user registration and login.

### Fixed
- Resolved issue with incorrect password validation during login.

## [Week 4]

### Added
- Implemented functionality to add recipes.
- Integrated recipe management features with the UI.
- Implemented service layer for recipe management.
- Implemented functionality to display user's recipes on the UI.
- Added delete functionality for recipes.
- Added refresh functionality to update the UI after recipe deletion.

### Changed
- Updated UI to support recipe addition and display.
- Refactored repository classes to handle recipe-related operations.
- Modified database schema to include recipe table.

### Fixed
- Separated contents of index.py into ui files

## [Week 5]

### Added
- Implemented functionality to edit recipes.
- Integrated recipe management features with the UI, including recipe search and display.
- added random recipe generation button to "find recipes" page
- Implemented a service layer for recipe management.
- Added recipe search functionality based on name, ingredients, and maximum cooking time.
- Implemented functionality to display user's recipes on the UI.
- Added refresh functionality to update the UI after recipe deletion.
- Added UI for inspecting recipe details.
- started building prioritization for displayed recipes

  ## [Week 6]

### Added
- Docstring
- back buttons to pages
- input validation implemented for recipes

### Changed
- user interface enhanced with ttkthemes
  
### Fixed
- Application crashing when no recipes found
- recipe deletion
- only some results displayed
- username already in use message

    ## [Week 7]

### Added
- Randomly generated recipe is clickable
- Tests for RecipeAppService
- input validation added for user credentials

### Changed
- UI changes to add_recipe_page (buttons larger)

  ### Fixed
- fixed bug where editing targetted wrong recipes 

  





