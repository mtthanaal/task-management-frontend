from . import db
from .models import User, Task

def init_db():
    db.drop_all()
    db.create_all()

    # Create initial data
    user1 = User(username='thanaal20220062', password='MT020605')
    db.session.add(user1)
    db.session.commit()
