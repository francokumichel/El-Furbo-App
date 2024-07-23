from src.core.models.user.user import User
from src.core.bcrypt import bcrypt
from src.core.database import db

def create_user(**kwargs):
    if "password" in kwargs:
        hash = bcrypt.generate_password_hash(
            kwargs["password"].encode("utf-8"))
        kwargs.update(password=hash.decode("utf-8"))
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()
    return user
