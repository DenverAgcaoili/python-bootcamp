from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    now = datetime.now()
    return render_template("landing.html", hour=now.hour)

@app.route("/hobby/")
@app.route("/hobbies/")
def hobby():
    hobbies = ["going on hikes", "playing mobile games", "playing computer games"]
    return render_template("hobby.html", hobbies=hobbies)

@app.route("/opinion/<topic>")
@app.route("/opinions/<topic>")
def opinion(topic):
    return f"Whats your opinion on {topic}"

@app.route("/opinion/food")
def food():
    foods = ["adobo", "tinola", "sinigang", "sisig","bulalo"]
    return render_template("food.html", foods=foods)

@app.route("/skills/")
def skills():
    skill_levels = {
        "Working": "Beginner",
        "Avoiding work": "Advanced",
        "Sleeping": "Professional",
        "Working on site": "Poor",
        "Working from home": "Intermediate"
    }
    return render_template("skills.html", skills=skill_levels)

todo_items = ["laba", "kain", "ligo"]
@app.get("/todo/")
def get_todo():
    return render_template("todo.html", todos=todo_items)

@app.post("/todo/")
def post_todo():
    data_received = request.form["task"]
    todo_items.append(data_received)
    return redirect("/todo/")

app.run()