import click
from blog.database import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_simplelogin import SimpleLogin

def create_user(**data):
    """Create user with encrypted password"""
    if "username" not in data or "password" not in data:
        raise ValueError("Username and password are required")
    
    data["password"] = generate_password_hash(
        data.pop("password"), method="pbkdf2:sha256"
    )
    #TODO: verificar se o usuário ja existe
    mongo.db.users.insert_one(data)
    return data

def validate_login(user): #User é passado diretamente pelo login checker, caso queira colocar mais campos coloque login_form  
    print(user)
    """Validates user login"""
    if "username" not in user or "password" not in user:
        raise ValueError("Username and password are required")
    db_user = mongo.db.users.find_one({"username": user["username"]})
    if db_user and check_password_hash(db_user["password"],user["password"]):
        return True
    return False
    
def configure(app):
    SimpleLogin(app, login_checker=validate_login)
    
    @app.cli.command()
    @click.argument("username")
    @click.password_option()
    def add_user(username, password):
        """Creates a new user
        usage: flask add-user admin
        """
        user = create_user(username=username, password=password)
        click.echo(f"user created {user["username"]}")