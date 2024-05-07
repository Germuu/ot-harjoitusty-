# Architecture description

## Structure
Functionally distinct parts of the architecture are divided into a three-layer packaging structure shown below:

<img src="https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/class_diagram.png" alt="Application Logic Diagram" width="50%">

The **UI** package takes care of the user interface, **services** of the application logic, and **repositories** of the fetching and storage of data. Additionally, the **entities** package contains the classes *User* and *Recipe*, which define the relevant data items.

## User interface
The UI consists of 9 views:
- login
- register
- home
- my recipes
   - add recipe
   - edit recipe
- find recipes
  - search results
  - recipe details
    
The user interface (UI) of the application is structured into 9 distinct views, each implemented as its own class. Each view class is responsible for rendering the respective page's layout and handling user interactions within that page. By organizing the UI into separate classes, the codebase remains modular and easy to maintain, with a clear separation of concerns between different parts of the application. By the principle of separation of concerns, all logic is handled by calling methods contained in the *RecipeAppService* class.


## Application logic
The classes *User* and *Recipe* represent the user and recipe objects, which correspond to the contents of database tables:

```mermaid
classDiagram
    class User {
        username
        password
    }
    class Recipe {
        name
        cooking_time
        ingredients
        username
    }
    Recipe "*" -- "1" User
```
All functions initiated by the user are managed by the **RecipeAppService** class. Some methods provided by the class are:

```bash
register_user(self, username, password)
```

```bash
login(self, username, password)
```

```bash
get_current_user(self)
```

```bash
create_recipe(self, name, ingredients, time, username)
```

```bash
search_recipes_algorithm(self, name, ingredients, max_time, username)
```
RecipeAppService works as an interface between the UI and the repository classes.


## Data storage
The classes *RecipeRepository* and *UserRepository* of the **repositories** package handle the database interactions. Both classes handle data using an SQLite database.

Both users and recipes are stored in their respective database tables *users* and *recipes*. The database tables are initialized using the initialize_database.py file.

## Main functionalities
Some main functionalities will be highlighted using sequence diagrams.

### Login
```mermaid
sequenceDiagram
  actor User
  participant UI
  participant RecipeAppService
  participant UserRepository
  User ->> UI : Login button pressed
  UI ->> RecipeAppService : login("admin", "1234")
  RecipeAppService ->> UserRepository : find_by_username("admin")
  UserRepository ->> RecipeAppService : User
  RecipeAppService ->> UI : User
  UI ->> UI : _show_home_view()
```


1. The user interacts with the UI by pressing the login button.
2. The UI sends a login request to the RecipeAppService, passing the username ("admin") and password ("1234") as parameters.
3. The RecipeAppService receives the login request and communicates with the UserRepository to find the user with the provided username ("admin").
4. The UserRepository searches for the user in the database and returns the user object to the RecipeAppService.
5. The RecipeAppService receives the user object and sends it back to the UI.
6. The UI receives the user object and proceeds to show the home view to the user, indicating a successful login.

Overall, the sequence demonstrates the flow of interactions between the user, UI, RecipeAppService, and UserRepository during the login process, ultimately resulting in the presentation of the home view to the user upon successful authentication.

### Recipe search

```mermaid
sequenceDiagram
  participant User 
  participant UI as UI
  participant RecipeAppService 
  participant RecipeRepository 
  User ->> UI: Clicks search button
  UI ->> RecipeAppService: search_recipes_algorithm(name: "Chicken", max_time: 30, ingredients: "Tomato")
  RecipeAppService ->> RecipeRepository: search_recipes(name: "Chicken", max_time: 30, ingredients: "Tomato")
  RecipeRepository ->> RecipeAppService: results
  RecipeAppService ->> UI: results
  UI ->> UI: _show_results_view(self, results)
```

1. **User**: Initiates the search process by clicking the search button on the UI.
2. **UI**: Receives the search request from the user and forwards it to the RecipeAppService.
3. **RecipeAppService**: Processes the search request using the search_recipes_algorithm, passing the search filters: name="Chicken", max_time=30, and ingredients="Tomato".
4. **RecipeRepository**: Receives the search criteria from the RecipeAppService and executes the search_recipes method with the provided filters: name="Chicken", max_time=30, and ingredients="Tomato".
5. **RecipeRepository**: Retrieves the search results based on the specified criteria and sends them back to the RecipeAppService.
6. **RecipeAppService**: Receives the search results from the RecipeRepository.
7. **UI**: Displays the search results to the user by invoking the _show_results_view method, passing the retrieved results.
8. **UI**: Updates the view to show the search results to the user.

### Other functionalities
All user interactions in the application follow a similar logic:
- User triggers an action in the UI.
- UI invokes relevant methods in the RecipeAppService.
- RecipeAppService processes the action, accessing data if needed.
- UI updates based on the processed data.



