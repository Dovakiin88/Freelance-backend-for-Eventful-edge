from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id= db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable = False)
    last_name = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String, nullable = True, default = ' ')
    hoa = db.Column(db.String(200), nullable = False)
    phone_number = db.Column(db.String, nullable = False)
    g_auth_verify = db.Column(db.Boolean, default=False)
    token = db.Column(db.String, default = ' ', unique=True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first_name='', last_name='', password='', token='', hoa='', phone_number='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name= first_name
        self.last_name= last_name
        self.password= self.set_password(password)
        self.hoa= hoa
        self.phone_number= phone_number
        self.email= email
        self.token= self.set_token(24)
        self.g_auth_verify= g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'User {self.email} has been verified'
    
class Template(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(250), nullable=True)
    template_issue_number = db.Column(db.String, nullable = True)
    template_volume_number = db.Column(db.String, nullable = True)
    template_date = db.Column(db.String(50), nullable=True)
    template_hoa = db.Column(db.String(200), nullable=True)
    saved_template = db.Column(db.JSON)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)

    def __init__(self, name, template_issue_number, template_volume_number, template_date, template_hoa, user_token ):
        self.id= self.set_id()
        self.name= name
        self.template_issue_number= template_issue_number
        self.template_volume_number= template_volume_number
        self.template_date= template_date
        self.template_hoa= template_hoa
        self.user_token= user_token
    
    def __repr__(self):
        return f'{self.name} has been saved'
    
    def set_id(self):
        return (secrets.token_urlsafe())
    
class TemplateSchema(ma.Schema):
    class Meta:
        fields= ['id', 'name', 'template_issue_number', 'template_volume_number', 'template_date', 'template_hoa']

class UserSchema(ma.Schema):
    class Meta:
        fields = ['id', 'first_name', 'last_name', 'hoa', 'phone_number', 'email']

template_schema= TemplateSchema()
templates_schema=TemplateSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
