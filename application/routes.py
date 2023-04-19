#!/usr/bin/python
from datetime import datetime

from application import app
from flask import render_template

# ---------------------- User routes ----------------------


@app.route('/users')
def get_users():
    users = [{'name': 'Test User', 'id': 1}]
    return render_template("/users.html", users=users)


@app.route('/users/<int:user_id>')
def get_user(user_id):
    user = {'name': 'Test user',
            'id': 1,
            'created_at': datetime.fromisoformat('2023-04-19T10:30:00'),
            'updated_at': datetime.fromisoformat('2023-04-19T10:30:00'),
            'cats': [
                {'name': 'Test cat', 'id': 1},
            ],
            }
    return render_template('user.html', user=user)


# # ---------------------- Cat routes ----------------------


@app.route('/cats')
def get_cats():
    cats = [{'name': 'Test cat', 'id': 1, 'owner': {'name': 'Test User', 'id': 1}}]
    return render_template("/cats.html", cats=cats)


@app.route('/cats/<int:cat_id>')
def get_cat(cat_id):
    cat = {'name': 'Test cat',
           'id': 1,
           'created_at': datetime.fromisoformat('2023-04-19T10:30:00'),
           'updated_at': datetime.fromisoformat('2023-04-19T10:30:00'),
           'owner': {
               'id': 1,
               'name': 'Test user',
           }
           }
    return render_template('cat.html', cat=cat)


@app.route('/')
def index():
    users_count = 1
    cats_count = 1

    return render_template('index.html', users_count=users_count, cats_count=cats_count)

