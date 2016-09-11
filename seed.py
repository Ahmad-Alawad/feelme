"""Utility file to seed ratings database from MovieLens data in seed_data/"""

import datetime
from sqlalchemy import func

from model import User, Post, Comment, connect_to_db, db
from server import app


def load_users():
    """Load fake users"""

    print "Users"

    user1 = User(email='ahmad1@gmail.com', password='123')
    user2 = User(email='ahmad2@gmail.com', password='123')
    user3 = User(email='ahmad3@gmail.com', password='123')
    user4 = User(email='ahmad4@gmail.com', password='123')
    # We need to add to the session or it won't ever be stored
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    # Once we're done, we should commit our work
    db.session.commit()


def load_posts():
    """Load fake posts"""

    print "Users"

    post1 = Post(title='I feel sick', body='Yesterday\nI felt sick', user_id=1)
    post2 = Post(title='I miss my BF', body='He is away\nand I miss him', user_id=2)
    post3 = Post(title='beh beh beh', body='behbehbeh\nhehehehhe\nbehebhebh', user_id=1)
    post4 = Post(title='meh meh meh', body='mooooooo\neoooooooooo\nhoooooooooo', user_id=2)

    # We need to add to the session or it won't ever be stored
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)

    # Once we're done, we should commit our work
    db.session.commit()


def load_comments():
    """Load fake comments"""

    print "Users"

    comment1 = Comment(body='some comment from user 3', user_id=3, post_id=1)
    comment2 = Comment(body='some comment from user 3', user_id=3, post_id=2)
    comment3 = Comment(body='some comment from user 4', user_id=4, post_id=3)
    comment4 = Comment(body='some comment from user 4', user_id=4, post_id=4)

    # We need to add to the session or it won't ever be stored
    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.add(comment4)

    # Once we're done, we should commit our work
    db.session.commit()


def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_users()
    load_posts()
    load_comments()
    set_val_user_id()
