from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

# Dictionary to store subject marks
marks = {'Maths': 80, 'Science': 75, 'English': 85}

# Student information
name = 'John Doe'
roll_no = '123456'

@app.route('/')
def my_marks():
    return render_template('index.html', marks=marks, name=name, roll_no=roll_no)

@app.route('/marks/<subject>')
def subject_marks(subject):
    if subject in marks:
        return render_template('index.html', subject=subject, marks=marks[subject], name=name, roll_no=roll_no)
    else:
        return render_template('index.html', subject=subject, name=name, roll_no=roll_no)

@app.route('/marks/<subject>/update', methods=['GET', 'POST'])
def update_marks(subject):
    if subject in marks:
        if request.method == 'POST':
            new_marks = request.form['marks']
            marks[subject] = int(new_marks)
            return redirect(url_for('subject_marks', subject=subject))
        else:
            return render_template('update.html', subject=subject, marks=marks[subject])
    else:
        return render_template('index.html', subject=subject, name=name, roll_no=roll_no)

@app.route('/marks/<subject>/delete', methods=['POST'])
def delete_marks(subject):
    if subject in marks:
        del marks[subject]
    return redirect(url_for('my_marks'))

@app.route('/add_subject', methods=['POST'])
def add_subject():
    new_subject = request.form['subject']
    new_marks = request.form['marks']
    marks[new_subject] = int(new_marks)
    return redirect(url_for('my_marks'))

if _name_ == '_main_':
    app.run(debug=True)