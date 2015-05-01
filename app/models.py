from app import db

class user_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64))
    post = db.Column(db.Text())

    def __init__(self, author, post):
        self.author = author
        self.post = post

    def __repr__(self):
        return '<User %r>' % (self.author)

class photo(db.Model):
    photo_id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.Text())

    def __init__(self, photo_url):
        self.photo_url = photo_url
        
    def __repr__(self):
    	return '<Photo %r>' % (self.photo_url)

class chinese_user_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64))
    post = db.Column(db.Text())

    def __init__(self, author, post):
        self.author = author
        self.post = post

    def __repr__(self):
        return '<User %r>' % (self.author)

db.create_all()