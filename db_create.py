from app import db
from app.models import * 

db.create_all()

#inserting
db.session.add(user_post("jack", "yoyoyooyoyoyoyo"))

#commiting
db.session.commit()