from app import db

class User(db.Model):
    # have the following columns
    # id (int)
    # author (string, unique, can't be null)pip install flask-wtf flask-sqlalchemy flask-login
    # message (linkd to Messages table)
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String, nullable=False, unique=True)
    message = db.relationship('Messages', backref='author', lazy='dynamic' )
    
    def check_author(self, author):
        #Check if the author exits in database or not
        #then return False for not and True for exist 
        if author != self.author:
            return False
        return True
    def __repr__(self):
        return f'<User {self.author}>'

class Messages(db.Model):
    # have the following columns
    # id (int)
    # message (string, not unique, can't be null)
    # user_id link to id (int)
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # write __repr__ that outputs
    # <Message: MESSAGE_GOES_HERE>
    # replace MESSAGE_GOES_HERE with the message
    def __repr__(self):
        return f'<Message: {self.message}>'
db.create_all()
db.session.commit()