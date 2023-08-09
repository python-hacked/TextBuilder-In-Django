# TextBuilder-In-Django

This Django project provides a simple web application for transforming text using different operations such as converting to uppercase, converting to lowercase, and clearing the text. The transformed texts are displayed in a list on the page.

## Features

- Transform text to uppercase
- Transform text to lowercase
- Clear the text
- Display a list of recently transformed texts

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/python-hacked/TextBuilder-In-Django.git`.
2. Create a virtual environment: `python -m venv venv`.
3. Activate the virtual environment:
    - On Windows: `venv\Scripts\activate`
    - On macOS and Linux: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`.
5. Run migrations: `python manage.py migrate`.
6. Start the development server: `python manage.py runserver`.

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/home`.
2. Enter text in the text area.
3. Click the "UpperCase" button to transform the text to uppercase.
4. Click the "LowerCase" button to transform the text to lowercase.
5. Click the "Clear" button to clear the text area.
6. Transformed texts will be displayed in a list below the buttons.

## NOTE
hear is 2 templates file first i am use javascripts and the url is `http://127.0.0.1:8000/`
then secand file i am use only python code and the url is `http://127.0.0.1:8000/home`
