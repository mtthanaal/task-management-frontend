from . import db
from .models import User, Task

def init_db():
    db.drop_all()
    db.create_all()

    # Create initial data
    user1 = User(username='teamlead', password='password')
    db.session.add(user1)
    db.session.commit()
