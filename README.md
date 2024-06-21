# Sticky Notes and Bulletin Board Application

This is a Django application that allows users to create, view, edit, and delete sticky notes and bulletin board posts.

## Features

- Create, view, edit, and delete sticky notes
- Create, view, edit, and delete bulletin board posts
- Simple and intuitive user interface
- Search functionality for notes and posts

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/NattSpeight/NattSpeight-StickyNoteApplication.git
    cd Sticky_Notes
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
