from app import db

class user_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64))
    post = db.Column(db.Text())

    def __repr__(self):
        return '<User %r>' % (self.author)