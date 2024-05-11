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
<img width="155" alt="image" src="https://github.com/Germuu/ot-harjoitustyo/assets/134619165/c40a2082-1bac-4585-8b9c-1033f04a07aa">













