from project import db

# create the database
db.create_all()


# commit the changes
db.session.commit()
