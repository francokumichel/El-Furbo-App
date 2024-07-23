from flask import Blueprint, render_template
from src.core.models import user

users_blueprint = Blueprint("users", __name__, url_prefix="/users")

@users_blueprint.get("/")
def user_index():
    return render_template("users/users_list.html", users=user.list_users())