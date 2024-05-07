# Architecture description

## Structure
Functionally distinct parts of the architecture are divided into a three-layer packaging structure shown below:
![Application Logic Diagram](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/class_diagram.png)

The UI package takes care of the user interface, services of the application logic, and repositories of the fetching and saving of data. Additionally, the entities package contains the classes **User** and **Recipe**, which define the relevant data items.

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

## Sequence diagram for login

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





