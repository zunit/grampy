import os
from flask import render_template, flash, redirect, url_for
from app import app
from app import db, models
from flask import request
from config import POSTS_PER_PAGE, UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from werkzeug import secure_filename
import random
import string

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
	users = models.user_post.query.order_by(models.user_post.id.desc()).paginate(page, POSTS_PER_PAGE, False)
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
 		users = models.user_post.query.order_by(models.user_post.id.desc()).paginate(1, POSTS_PER_PAGE, False)
 		return render_template('eng_note.html',
                           users=users, title='Grandpa')

@app.route('/delete/<uid>', methods=['GET','POST'])
def delete_post(uid):
	print(uid)
	del_user = models.user_post.query.filter_by(id=uid).first()
	print(del_user)
	print("went in to delete")
	db.session.delete(del_user)
	db.session.commit()
	users = models.user_post.query.order_by(models.user_post.id.desc()).paginate(1, POSTS_PER_PAGE, False)
	return render_template('eng_note.html',
                           users=users, title='Grandpa')

@app.route('/editpage/<uid>', methods=['GET','POST'])
def edit_page(uid):
	edit_user = models.user_post.query.filter_by(id=uid).first()
	print('EDITING')
	return render_template('eng_edit_note.html',
                           user=edit_user, title='Grandpa')

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
	users = models.user_post.query.order_by(models.user_post.id.desc()).paginate(1, POSTS_PER_PAGE, False)
	return render_template('eng_note.html',
                           users=users, title='Grandpa')

# TODO - Picture Uploading -> Gallery Page
# check that filename is of appropriate image type
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			name = (
				''.join(
					random.SystemRandom().choice(
						string.ascii_uppercase + string.digits) for _ in range(25))) + os.path.splitext(
				file.filename)[1]
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
			# initiate the db
			print("filename is: " + name)
			pic = models.photo(photo_url=name)	
			db.session.add(pic)
			db.session.commit()
			print("uploaded")
		else:
			# file doesn't exist or work 
			message = "no Pictures Uploaded"
			return redirect(url_for('gallery'))
	return redirect(url_for('gallery'))


@app.route('/gallery')
def gallery():
	photos = models.photo.query.all()
	return render_template('gallery.html', title='Grandpa', photos=photos)

@app.route('/remove_photo')
def remove_photo():
	photos = models.photo.query.all()
	return render_template('del_image.html', title='Grandpa', photos=photos)

@app.route('/delete_image/<pid>', methods=['GET','POST'])
def delete_image(pid):
	print(pid)
	del_image = models.photo.query.filter_by(photo_id=pid).first()
	os.remove(os.path.join(app.config['UPLOAD_FOLDER'], del_image.photo_url))
	print(del_image)
	print("went in to delete")
	db.session.delete(del_image)
	db.session.commit()
	photos = models.photo.query.all()
	return render_template('del_image.html', title='Grandpa', photos=photos)

################# CHINESE VERSION #################
@app.route('/chinese_note', methods=['GET', 'POST'])
@app.route('/chinese_note/<int:page>', methods=['GET', 'POST'])
def chinese_version(page=1):

	# the page number, starting from 1
	# the number of items per page
	# an error flag. If True, when an out of range page is requested a 
	# 404 error will be automatically returned
	users = models.chinese_user_post.query.order_by(models.chinese_user_post.id.desc()).paginate(page, POSTS_PER_PAGE, False)
	return render_template('chinese_note.html',
                           users=users, title='Grandpa')

@app.route('/chinese_add', methods=['POST'])
def chinese_create_post():
 	if request.method == 'POST':
 		# flash('New entry was successfully posted')
 		name = request.form.get('name')
 		posting = request.form.get('posting')
 		
 		if (name) and (posting):
			#print("name: " + name)
 			#print("posting: " + posting)
 			posted = models.chinese_user_post(author=name, post=posting)
 			db.session.add(posted)
 			db.session.commit()
 		else:
 			print("NOTHING")
 		users = models.chinese_user_post.query.order_by(models.chinese_user_post.id.desc()).paginate(1, POSTS_PER_PAGE, False)
 		return render_template('chinese_note.html',
                           users=users, title='Grandpa')

@app.route('/chinese_edit_page/<uid>', methods=['GET','POST'])
def chinese_edit_page(uid):
	edit_user = models.chinese_user_post.query.filter_by(id=uid).first()
	print('EDITING')
	return render_template('chinese_edit_note.html',
                           user=edit_user, title='Grandpa')

@app.route('/chinese_edit/54189152453208840160575909244032836966034231<uid>4017583302733497112593271406405136426945904196334790299', methods=['GET','POST'])
def chinese_edit_post(uid):
	edit_user = models.chinese_user_post.query.filter_by(id=uid).first()
	name = request.form.get('name')
 	posting = request.form.get('posting')
 	print(uid)
	if (name):
		edit_user = models.chinese_user_post.query.filter_by(id=uid).update({"author": name})
	if (posting):
		edit_user = models.chinese_user_post.query.filter_by(id=uid).update({"post": posting})
	db.session.commit()
	users = models.chinese_user_post.query.order_by(models.chinese_user_post.id.desc()).paginate(1, POSTS_PER_PAGE, False)
	return render_template('chinese_note.html',
                           users=users, title='Grandpa')

@app.route('/chinese_delete/<uid>', methods=['GET','POST'])
def chinese_delete_post(uid):
	print(uid)
	del_user = models.chinese_user_post.query.filter_by(id=uid).first()
	print(del_user)
	print("went in to delete")
	db.session.delete(del_user)
	db.session.commit()
	users = models.chinese_user_post.query.order_by(models.chinese_user_post.id.desc()).paginate(1, POSTS_PER_PAGE, False)
	return render_template('chinese_note.html',
                           users=users, title='Grandpa')

@app.route('/chinese_gallery')
def chinese_gallery():
	photos = models.photo.query.all()
	return render_template('chinese_gallery.html', title='Grandpa', photos=photos)

@app.route('/chinese_remove_photo')
def chinese_remove_photo():
	photos = models.photo.query.all()
	return render_template('chinese_del_image.html', title='Grandpa', photos=photos)

@app.route('/chinese_delete_image/<pid>', methods=['GET','POST'])
def chinese_delete_image(pid):
	print(pid)
	del_image = models.photo.query.filter_by(photo_id=pid).first()
	os.remove(os.path.join(app.config['UPLOAD_FOLDER'], del_image.photo_url))
	print(del_image)
	print("went in to delete")
	db.session.delete(del_image)
	db.session.commit()
	photos = models.photo.query.all()
	return render_template('chinese_del_image.html', title='Grandpa', photos=photos)

@app.route('/chinese_upload', methods=['GET', 'POST'])
def chinese_upload():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			name = (
				''.join(
					random.SystemRandom().choice(
						string.ascii_uppercase + string.digits) for _ in range(25))) + os.path.splitext(
				file.filename)[1]
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
			# initiate the db
			print("filename is: " + name)
			pic = models.photo(photo_url=name)	
			db.session.add(pic)
			db.session.commit()
			print("uploaded")
		else:
			# file doesn't exist or work 
			message = "no Pictures Uploaded"
			return redirect(url_for('chinese_gallery'))
	return redirect(url_for('chinese_gallery'))
