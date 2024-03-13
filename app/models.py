# Creates User class to be stored as an entry in database db from __init__.py
# * User class uses template from db.Model (a base class for all models from Flask-SQLAlchemy)
# * Optional typing hint from Python imported for optional input for a field as shown in password_hash (input can be null or a hash value)
# * mapped_column() functions have additional configurations to specify string input lenghts, primary keys, 
#   as well as indexed and unique fields (these help with consistent efficient database searches)
# * __repr__ method tells Python how to print these class objects (helpful for debugging)
#
# * to initialize db, input:
#   $ flask db init
# * to migrate the db in event of new models or new relationships in db, input:
#   $ flask db migrate -m "<ENTER DESCRIPTION OF MIGRATION>"
#   $ flask db upgrade
from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    
    author: so.Mapped[User] = so.relationship(back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)