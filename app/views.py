from flask import render_template, flash
from app import app
from app import db, models
from flask import request
from config import POSTS_PER_PAGE

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Dear Grandpa')

@app.route('/eng_note', methods=['GET', 'POST'])
@app.route('/eng_note/<int:page>', methods=['GET', 'POST'])
def eng_version(page=1):

	# the page number, starting from 1
	# the number of items per page
	# an error flag. If True, when an out of range page is requested a 
	# 404 error will be automatically returned
	users = models.user_post.query.paginate(page, POSTS_PER_PAGE, False)
	return render_template('eng_note.html',
                           users=users, title='Grandpa')

@app.route('/add', methods=['POST'])
def create_post():
 	if request.method == 'POST':
 		# flash('New entry was successfully posted')
 		name = request.form.get('name')
 		posting = request.form.get('posting')
 		
 		if (name) and (posting):
			print("name: " + name)
 			print("posting: " + posting)
 			posted = models.user_post(author=name, post=posting)
 			db.session.add(posted)
 			db.session.commit()
 		else:
 			print("NOTHING")
 		users = models.user_post.query.all()
 		return render_template('eng_note.html',
                           users=users, title='Dear Grandpa')

@app.route('/delete/<uid>', methods=['GET','POST'])
def delete_post(uid):
	print(uid)
	del_user = models.user_post.query.filter_by(id=uid).first()
	print(del_user)
	print("went in to delete")
	db.session.delete(del_user)
	db.session.commit()
	users = models.user_post.query.all()
	return render_template('eng_note.html',
                           users=users, title='Dear Grandpa')

@app.route('/editpage/<uid>', methods=['GET','POST'])
def edit_page(uid):
	edit_user = models.user_post.query.filter_by(id=uid).first()
	print('EDITING')
	return render_template('eng_edit_note.html',
                           user=edit_user, title='Dear Grandpa')

@app.route('/edit/54189152453208840160575909244032836966034231<uid>4017583302733497112593271406405136426945904196334790299', methods=['GET','POST'])
def edit_post(uid):
	edit_user = models.user_post.query.filter_by(id=uid).first()
	name = request.form.get('name')
 	posting = request.form.get('posting')
 	print(uid)
	if (name):
		edit_user = models.user_post.query.filter_by(id=uid).update({"author": name})
	if (posting):
		edit_user = models.user_post.query.filter_by(id=uid).update({"post": posting})
	db.session.commit()
	users = models.user_post.query.all()
	return render_template('eng_note.html',
                           users=users, title='Dear Grandpa')

# TODO - Picture Uploading -> Gallery Page






