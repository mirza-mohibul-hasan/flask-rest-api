from app import app
from model.user_model import user_model
@app.route("/user/signup")
def user_signup_controller():
    return user_model.user_signup_model()