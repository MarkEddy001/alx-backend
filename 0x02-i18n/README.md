# 0x02. i18n

## Curriculum
- Short Specializations
- Average: 141.24%

## Project Timeline
- **Project Start:** Aug 27, 2024, 6:00 AM
- **Project End:** Aug 28, 2024, 6:00 AM
- **Checker Release:** Aug 27, 2024, 12:00 PM
- **Manual QA Review:** Request when done
- **Auto Review:** Launched at the deadline

## Resources
- [Flask-Babel](https://pythonhosted.org/Flask-Babel/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz](https://pythonhosted.org/pytz/)

## Learning Objectives
- Parametrize Flask templates to display different languages.
- Infer the correct locale based on URL parameters, user settings, or request headers.
- Localize timestamps.

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- A `README.md` file at the root of the project is mandatory.
- Code should use the `pycodestyle` style (version 2.5).
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- All `*.py` files should be executable.
- All modules should have documentation.
- All classes should have documentation.
- All functions and methods should have documentation.
- All functions and coroutines must be type-annotated.

## Tasks

### 0. Basic Flask app
- **File:** `0-app.py`, `templates/0-index.html`
- **Description:** Setup a basic Flask app with a single `/` route and an `index.html` template that outputs “Welcome to Holberton” as the page title and “Hello world” as the header.

### 1. Basic Babel setup
- **File:** `1-app.py`, `templates/1-index.html`
- **Description:** Install Flask-Babel and configure it with a `Config` class that sets available languages to `["en", "fr"]`, default locale to `"en"`, and timezone to `"UTC"`.

### 2. Get locale from request
- **File:** `2-app.py`, `templates/2-index.html`
- **Description:** Create a `get_locale` function using the `babel.localeselector` decorator to determine the best match with supported languages.

### 3. Parametrize templates
- **File:** `3-app.py`, `babel.cfg`, `templates/3-index.html`, `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po`, `translations/en/LC_MESSAGES/messages.mo`, `translations/fr/LC_MESSAGES/messages.mo`
- **Description:** Use `_` or `gettext` to parametrize templates. Initialize translations and compile dictionaries.

### 4. Force locale with URL parameter
- **File:** `4-app.py`, `templates/4-index.html`
- **Description:** Implement a way to force a particular locale using the `locale` URL parameter.

### 5. Mock logging in
- **File:** `5-app.py`, `templates/5-index.html`
- **Description:** Mock a user login system using a user table and display a welcome message if a user is logged in.

### 6. Use user locale
- **File:** `6-app.py`, `templates/6-index.html`
- **Description:** Modify `get_locale` to use a user’s preferred locale if supported.

### 7. Infer appropriate time zone
- **File:** `7-app.py`, `templates/7-index.html`
- **Description:** Define a `get_timezone` function to infer the time zone from URL parameters, user settings, or default to UTC.

### 8. Display the current time
- **File:** `app.py`, `templates/index.html`, `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po`
- **Description:** Display the current time on the home page based on the inferred time zone.

## License
This project is licensed under the terms of the ALX license.
