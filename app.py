import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))


def calculate(a, b):
    """
    Returns the result of a simple calculation with two numbers.
    Parameters
    ----------
    a : float or int
        The first number in the calculation.
    b : float or int
        The second number in the calculation.
    Returns
    -------
    float or int
        The result of the calculation.
    """
    return a + b



def add_user(username, password):
    """Add a new user to the database.

    Parameters:
        username (str): The username of the new user.
        password (str): The plaintext password of the new user.

    Returns:
        None: If the user is successfully added.
        str: Error message if there was an issue adding the user.
    """
    # Connect to database and create cursor
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Check if username already exists
    check_user = c.execute(f"SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    if check_user is not None:
        return f"Username {username} already exists."

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert new user into database
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))

    # Commit changes and close cursor
    conn.commit()
    c.close()



"""
    This function takes two arguments and returns their sum.

    :param first_num: (float) The first number to be added.
    :param second_num: (float) The second number to be added.
    :return: (float) The sum of the two numbers.
    """
    return first_num + second_num
TESTS:

def calculate(a, b):
    """
    Returns the result of a simple calculation with two numbers.
    """
    return a + b

TESTS: