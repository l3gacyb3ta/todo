
# Create a flask server 
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask import make_response, flash
from flask import session as login_session
import sqlite3

app = Flask(__name__)


def query():
    """Get all entries in the sqlite database"""
    with sqlite3.connect('todo.db') as connection:
        c = connection.cursor()
        c.execute("SELECT * FROM todo")
        items = c.fetchall()
        return items

def create_entry(name: str):
    """Create a new entry in the sqlite database"""
    with sqlite3.connect('todo.db') as connection:
        c = connection.cursor()
        c.execute("INSERT INTO todo (TASK, DONE) VALUES (?, ?)", (name, "false"))
        connection.commit()

@app.route('/')
def index():
    """Load data from database and return it through a jinja template"""
    return render_template('index.html')

@app.route('/items')
def get_items():
    """Render the template with all the current todos"""
    items = query()
    return render_template('items.html', items=items)

@app.route('/items/new', methods=['GET', 'POST'])
def create_item():
    """Create a new todo item"""
    if request.method == 'POST':
        create_entry(request.form['name'])
        return redirect(url_for('get_items'))
    else:
        return render_template('new_item.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000)
