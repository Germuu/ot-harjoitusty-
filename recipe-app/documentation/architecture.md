```mermaid
classDiagram
    RecipeAppService "0..1" -- package "Entities" {
        class User
        class Recipe
    }
    User "1" -- "*" Recipe

     
    

```
