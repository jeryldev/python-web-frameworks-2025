from django.shortcuts import render

# Our in-memory database
todos = [
    {"id": 1, "title": "Learn Django basics", "completed": False},
    {"id": 2, "title": "Create a simple Todo app", "completed": False},
    {"id": 3, "title": "Understand Django templates", "completed": True},
]

# Counter for new IDs
next_id = 4


def todo_list(request):
    global todos, next_id

    # Handle form submissions
    if request.method == "POST":
        # Add new todo
        if "add" in request.POST:
            title = request.POST.get("title")
            if title:
                todos.append({"id": next_id, "title": title, "completed": False})
                next_id += 1

        # Toggle todo status
        elif "toggle" in request.POST:
            todo_id = int(request.POST.get("toggle"))
            for todo in todos:
                if todo["id"] == todo_id:
                    todo["completed"] = not todo["completed"]

        # Delete todo
        elif "delete" in request.POST:
            todo_id = int(request.POST.get("delete"))
            todos = [todo for todo in todos if todo["id"] != todo_id]

    # Sort todos (incomplete first)
    sorted_todos = sorted(todos, key=lambda x: x["completed"])

    return render(request, "todos/todo_list.html", {"todos": sorted_todos})
