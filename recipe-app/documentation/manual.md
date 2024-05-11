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
















