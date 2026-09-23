#step1: imports
# pip install Flask Flask-SQLAlchemy

from flask import Flask, render_template, request, redirect, url_for

from flask_wtf import FlaskForm

#FLASK EXTENSION #2: Flask-SQLAlchemy (database access + ORM)
from flask_sqlalchemy import SQLAlchemy

from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired,InputRequired, NumberRange

#step2 : bulit app
app = Flask(__name__)

#step3: security key
# Required by Flask-WTF for CSRF protection (change for real projects use private key)
app.config["SECRET_KEY"] = "my-demo-key"

#step4: Database
# Tells Flask-SQLAlchemy which database to use.
# "sqlite:///students.db" means: a SQLite file named students.db (created automatically)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"

# Create the database object and connect it to the flask app
database = SQLAlchemy(app)


# MODEL: this class IS the database table structure (ORM mapping of flask)
class Student(database.Model):
    id = database.Column(database.Integer, primary_key=True)   # unique id, auto-generated
    name = database.Column(database.String(50), nullable=False)
    course = database.Column(database.String(50), nullable=False)
    marks = database.Column(database.Integer, nullable=False)


# step5: Form definition (uses Flask-WT Form)
class StudentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    course = StringField("Course", validators=[DataRequired()])
    marks = IntegerField("Marks", validators=[InputRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField("Add Student")


#step6:  Page 1: list + search
@app.route("/")
def index():
    search_text = request.args.get("search", "")

    if search_text:
        # SELECT * FROM student WHERE name LIKE 'sakina'
        matching_students = Student.query.filter(
            Student.name.ilike(f"%{search_text}%")
        ).all()
    else:
        # SELECT * FROM student
        matching_students = Student.query.all()

    return render_template("index.html", students=matching_students, search_text=search_text)


#step7: Page 2: add a new student
@app.route("/add", methods=["GET", "POST"])
def add_student():
    form = StudentForm()

    if form.validate_on_submit():
        # Create a Python object (one future row)
        new_student = Student(
            name=form.name.data,
            course=form.course.data,
            marks=form.marks.data,
        )
        database.session.add(new_student)      # stage it (INSERT is prepared)
        database.session.commit()              # save it permanently to the database
        return redirect(url_for("index"))

    return render_template("add.html", form=form)


#step8: Create the table and add starting data (runs once at startup)
with app.app_context():
    database.create_all()                      # CREATE TABLE student (if it doesn't exist)

    if Student.query.count() == 0:             # only add sample data if table is empty
        database.session.add_all([
            Student(name="Ghishu", course="Python", marks=88),
            Student(name="Ravi", course="cs699", marks=72),
            Student(name="Meera", course="chemistry", marks=45),
            Student(name="SAKINA", course="Physics", marks=88),
            Student(name="RAJIV", course="Physics", marks=72),
            Student(name="Manoj", course="History", marks=45),
            Student(name="sunil", course="chemistry", marks=88),
            Student(name="Rohan", course="Biology", marks=72),
            Student(name="siva", course="chemistry", marks=45),
        ])
        database.session.commit()


if __name__ == "__main__":
    app.run(debug=True)