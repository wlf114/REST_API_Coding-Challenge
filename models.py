from config import db, ma
  
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)
    
class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    archive = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #user = db.relationship("User", back_populates = "task")

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session

class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task
        sqla_session = db.session
