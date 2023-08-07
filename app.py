from Vive import app, db
from flask_login import LoginManager
from models import User
from routes import Login, registration, dashboard, logout, Forgot_Password

login_manager= LoginManager()
login_manager.init_app(app) # this initializes the app called app
login_manager.login_view = "Login" #this creates an endpoint for when an unathorized user tries to access a restricted page

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
