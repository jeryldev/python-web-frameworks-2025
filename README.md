# Python Web Frameworks: Django vs FastAPI

A beginner-friendly comparison of Django and FastAPI for modern web development.

This repository contains materials for a presentation comparing Django and FastAPI, designed for college students learning about web development frameworks. It includes two identical Todo applications built with each framework to demonstrate different implementation approaches for the same functionality.

## Repository Structure

```
python-web-frameworks-2025/
├── README.md                       # This file
├── presentation/                   # Presentation materials
│   ├── Presentation.pptx           # PowerPoint slides
│   ├── Presentation.pdf            # Presentation pdf
│   └── images/                     # SVG diagrams and other images used in slides
│       ├── django-request-flow.svg
│       ├── fastapi-request-flow.svg
│       └── ...
├── django_sample/                  # Django Todo application
│   ├── db.sqlite3                  # SQLite database
│   ├── django_todo/                # Django project files
│   ├── manage.py                   # Django management script
│   ├── static/                     # Static files (CSS, JS)
│   ├── templates/                  # HTML templates
│   ├── todos/                      # Todo app
│   └── venv/                       # Virtual environment (not tracked in git)
├── fastapi_sample/                 # FastAPI Todo application
│   ├── main.py                     # Main FastAPI application
│   ├── static/                     # Static files (CSS, JS)
│   ├── templates/                  # HTML templates
│   └── venv/                       # Virtual environment (not tracked in git)
└── code-snippets/                  # Code snippets for side-by-side comparison
```

## Running the Django Sample

The Django sample is a simple Todo application that demonstrates Django's architecture and features.

### Setup

1. Navigate to the Django sample directory:

   ```
   cd django_sample
   ```

2. Create and activate a virtual environment:

   ```
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   # Or if requirements.txt is not available:
   pip install django django-htmx
   ```

4. Apply migrations to set up the database:
   ```
   python manage.py migrate
   ```

### Running the Server

Start the Django development server on port 8000:

```
python manage.py runserver 8000
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to see the application.

## Running the FastAPI Sample

The FastAPI sample is a functionally identical Todo application that demonstrates FastAPI's approach.

### Setup

1. Navigate to the FastAPI sample directory:

   ```
   cd fastapi_sample
   ```

2. Create and activate a virtual environment:

   ```
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   # Or if requirements.txt is not available:
   pip install fastapi uvicorn jinja2 python-multipart
   ```

### Running the Server

Start the FastAPI server on port 8001:

```
# Using Python directly
python main.py

# Or using uvicorn directly
uvicorn main:app --reload --port 8001
```

Visit [http://127.0.0.1:8001/](http://127.0.0.1:8001/) in your browser to see the application.

## Features Demonstrated

Both applications implement the same features to demonstrate different implementation approaches:

- Adding new todo items
- Toggling completion status
- Deleting todo items

## Key Differences Highlighted

The implementations highlight several key differences between the frameworks:

- **Project Structure**: Django's project/app organization vs FastAPI's simpler structure
- **Routing**: Django's URL patterns vs FastAPI's decorator-based routes
- **Templates**: Django Template Language vs Jinja2 templates
- **Request Handling**: Django's view functions vs FastAPI's typed route handlers
- **API Documentation**: FastAPI's automatic docs vs Django's manual approach

## Presentation Materials

The `presentation` directory contains slides and diagrams used in the presentation. Feel free to use these materials for educational purposes.

## Note for Presenters

If you're presenting this material:

1. Run both servers simultaneously (on different ports) for a side-by-side comparison
2. Familiarize yourself with the flow guide in the presentation notes
3. Consider running through the demo once before the actual presentation

## Resources for Further Learning

- [Django Documentation](https://docs.djangoproject.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)
- [Mozilla Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [TestDriven.io FastAPI Tutorials](https://testdriven.io/blog/topics/fastapi/)
- [freeCodeCamp's Python Courses](https://www.freecodecamp.org/learn/)

## License

This project is open source and available under the [MIT License](LICENSE).
