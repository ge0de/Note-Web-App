# required libraries for the epic project
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notepad.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models to Implement
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    notes = db.relationship('Note', backref='user', lazy=True)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Required Routes
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        if User.query.filter_by(username=username).first():
            flash('Username exists.', 'error')
            return redirect(url_for('register'))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registered. Please Log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Logged in.', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials. Try again.', 'error')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = User.query.get(user_id)

    if request.method == 'POST':
        note_content = request.form['content']
        new_note = Note(content=note_content, user_id=user_id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added.', 'success')

    notes = Note.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', notes=notes, username=user.username)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out.', 'info')
    return redirect(url_for('login'))

# edit & delete, important routes

@app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    note = Note.query.get(note_id)

    if note is None or note.user_id != user_id:
        return redirect(url_for('dashboard'))  # Unauthorized access if note doesn't belong to the user

    if request.method == 'POST':
        note_content = request.form['content']
        note.content = note_content  # Update the note content
        db.session.commit()
        flash('Note updated.', 'success')
        return redirect(url_for('dashboard'))

    return render_template('edit_note.html', note=note)

@app.route('/delete_note/<int:note_id>', methods=['GET', 'POST'])
def delete_note(note_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    note = Note.query.get(note_id)

    if note is None or note.user_id != user_id:
        return redirect(url_for('dashboard'))
    # Prohibited access if note doesn't belong to the user

    db.session.delete(note)
    db.session.commit()
    flash('Note terminated.', 'danger')

    return redirect(url_for('dashboard'))

# Initialize Database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
