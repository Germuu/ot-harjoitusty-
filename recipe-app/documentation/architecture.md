```mermaid
classDiagram
    class User {
        <<Entities>>
        -id: int
        -username: string
        -password: string
    }
    class Todo {
        <<Entities>>
        -id: int
        -title: string
        -completed: boolean
    }
    class UserRepository {
        <<Repositories>>
        +findAll(): List<User>
        +findById(id: int): User
        +save(user: User): void
        +delete(user: User): void
    }
    class TodoRepository {
        <<Repositories>>
        +findAll(): List<Todo>
        +findById(id: int): Todo
        +save(todo: Todo): void
        +delete(todo: Todo): void
    }
    User "1" --> "*" Todo :
    UserRepository --|> User : 
    TodoRepository --|> Todo : 

```
