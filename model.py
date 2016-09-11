"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()


#####################################################################
# Model definitions

class User(db.Model):
    """User of ratings website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id,
                                               self.email)


class Post(db.Model):
    """Movie on ratings website."""

    __tablename__ = "posts"

    post_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    body = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer,
                         db.ForeignKey('users.user_id'))

    user = db.relationship("User",
                           backref=db.backref("posts",
                                              order_by=post_id))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Post post_id=%s title=%s>" % (self.post_id,
                                                 self.title)


class Comment(db.Model):
    """Movie on ratings website."""

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,
                         db.ForeignKey('users.user_id'))
    post_id = db.Column(db.Integer,
                         db.ForeignKey('posts.post_id'))

    user = db.relationship("User",
                           backref=db.backref("comments",
                                              order_by=comment_id))

    post = db.relationship("Post",
                           backref=db.backref("comments",
                                              order_by=comment_id))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Comment comment_id=%s>" % (self.comment_id)


#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feelme'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
