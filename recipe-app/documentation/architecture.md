```mermaid
classDiagram
    RecipeAppService "0..1" -- "0..1" User
    RecipeAppService "0..1" -- "0..1" Recipe
    User "1" -- Recipe "*"
