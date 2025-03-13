from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Our in-memory database
todos = [
    {"id": 1, "title": "Learn FastAPI basics", "completed": False},
    {"id": 2, "title": "Create a simple Todo app", "completed": False},
    {"id": 3, "title": "Understand Jinja2 templates", "completed": True},
]

# Counter for new IDs
next_id = 4


@app.get("/", response_class=HTMLResponse)
async def read_todos(request: Request):
    # Sort todos (incomplete first)
    sorted_todos = sorted(todos, key=lambda x: x["completed"])
    return templates.TemplateResponse(
        "todo_list.html", {"request": request, "todos": sorted_todos}
    )


@app.post("/add")
async def add_todo(title: str = Form(...)):
    global next_id
    if title:
        todos.append({"id": next_id, "title": title, "completed": False})
        next_id += 1
    return RedirectResponse(url="/", status_code=303)


@app.post("/toggle/{todo_id}")
async def toggle_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = not todo["completed"]
            break
    return RedirectResponse(url="/", status_code=303)


@app.post("/delete/{todo_id}")
async def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    return RedirectResponse(url="/", status_code=303)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
