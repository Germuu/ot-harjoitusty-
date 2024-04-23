## Application Logic

![Application Logic Diagram](https://github.com/Germuu/ot-harjoitustyo/blob/master/recipe-app/documentation/Pictures/class_diagram.png)

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





