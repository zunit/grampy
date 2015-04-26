from app import db

class user_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64))
    post = db.Column(db.Text())

    def __repr__(self):
        return '<User %r>' % (self.author)

class photo(db.Model):
	photo_id = db.Column(db.Integer, primary_key=True)
	photo_url=db.Column(db.Text)

	def __repr__(self):
		return '<User %r>' % (self.photo_url)