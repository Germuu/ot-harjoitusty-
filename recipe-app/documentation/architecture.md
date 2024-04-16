classDiagram
    class User {
        <<Entity>>
        -id: int
        -username: string
        -password: string
    }
    class Todo {
        <<Entity>>
        -id: int
        -title: string
        -completed: boolean
    }
    class UserRepository {
        <<Repository>>
        +findAll(): List<User>
        +findById(id: int): User
        +save(user: User): void
        +delete(user: User): void
    }
    class TodoRepository {
        <<Repository>>
        +findAll(): List<Todo>
        +findById(id: int): Todo
        +save(todo: Todo): void
        +delete(todo: Todo): void
    }
    User "1" --> "*" Todo : has
    UserRepository --|> User : contains
    TodoRepository --|> Todo : contains

