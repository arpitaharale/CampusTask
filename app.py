from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("campustask.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            deadline TEXT,
            priority TEXT,
            category TEXT,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def dashboard():

    conn = get_db()

    total = conn.execute(
        "SELECT COUNT(*) FROM tasks"
    ).fetchone()[0]

    pending = conn.execute(
        "SELECT COUNT(*) FROM tasks WHERE status = 'Pending'"
    ).fetchone()[0]

    completed = conn.execute(
        "SELECT COUNT(*) FROM tasks WHERE status = 'Completed'"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        total=total,
        pending=pending,
        completed=completed
    )


@app.route("/tasks")
def all_tasks():

    status = request.args.get("status")

    conn = get_db()

    if status in ["Pending", "Completed"]:
        tasks = conn.execute(
            "SELECT * FROM tasks WHERE status = ? ORDER BY deadline",
            (status,)
        ).fetchall()
    else:
        tasks = conn.execute(
            "SELECT * FROM tasks ORDER BY deadline"
        ).fetchall()

    conn.close()

    return render_template("tasks.html", tasks=tasks)


@app.route("/complete/<int:task_id>")
def complete_task(task_id):

    conn = get_db()

    conn.execute(
        "UPDATE tasks SET status = 'Completed' WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/tasks")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):

    conn = get_db()

    conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/tasks")


@app.route("/add-task", methods=["GET", "POST"])
def add_task():

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        deadline = request.form["deadline"]
        priority = request.form["priority"]
        category = request.form["category"]

        conn = get_db()

        conn.execute("""
            INSERT INTO tasks
            (title, description, deadline, priority, category, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            title,
            description,
            deadline,
            priority,
            category,
            "Pending"
        ))

        conn.commit()
        conn.close()

        return redirect("/tasks")

    return render_template("add_task.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)