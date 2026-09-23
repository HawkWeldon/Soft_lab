
from flask import Flask, render_template, request, redirect, url_for

# FLASK EXTENSION #1: Flask-WTF (form handling + CSRF protection)
from flask_wtf import FlaskForm

# WTForms (the library Flask-WTF is built on): fields and validators
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired,InputRequired, NumberRange

app = Flask(__name__)

# Public APIs: Do not need CSRF protection.
app.config["SECRET_KEY"] = "my-demo-key"

# In-memory temporary "database" dictionary - (resets when the server restarts)
students = [
    {"name": "Dulari", "course": "Python", "marks": 88},
    {"name": "Ravi", "course": "Flask", "marks": 72},
    {"name": "Meera", "course": "Django", "marks": 45},
    {"name": "SAKINA", "course": "Python", "marks": 88},
    {"name": "SAKINA", "course": "Python", "marks": 88},
    {"name": "Raj", "course": "Flask", "marks": 72},
    {"name": "Maya", "course": "Django", "marks": 45},
    {"name": "sunil", "course": "Python", "marks": 88},
    {"name": "RAJIV", "course": "Flask", "marks": 72},
    {"name": "prerna", "course": "Django", "marks": 45},
    {"name": "shneha", "course": "Python", "marks": 88},
    {"name": "pratik", "course": "Flask", "marks": 72},
    {"name": "siva", "course": "Django", "marks": 45},
]


# Form definition (uses Flask-WTF)
class StudentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    course = StringField("Course", validators=[DataRequired()])
    marks = IntegerField("Marks", validators=[InputRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField("Add Student")


# Page 1: list + search
@app.route("/")
def index():
    search_text = request.args.get("search", "")   # reads /?search=xyz

    if search_text:
        matching_students = [
            student for student in students
            if search_text.lower() in student["name"].lower()
        ]
        print("Matched students:", matching_students)
    else:
        matching_students = students

    return render_template("index.html", students=matching_students, search_text=search_text)


# Page 2: add a new student
@app.route("/add", methods=["GET", "POST"])
def add_student():
    form = StudentForm()

    # True only when the form was submitted, is valid, and the CSRF token is correct
    if form.validate_on_submit():
        students.append({
            "name": form.name.data,
            "course": form.course.data,
            "marks": form.marks.data,
        })
        return redirect(url_for("index"))

    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
