from flask import Blueprint, request, Flask, jsonify, render_template
from helpers import token_required
from models import db, User, Template, template_schema, templates_schema, user_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return{'Skyrim TEST': 'Awesomeness TEST'}

#Save template
@api.route('/savedte')

#add to database
@api.route('/templates', methods = ['POST'])
@token_required
def create_template(current_user_token):
    name = request.json['name']
    template_issue_number = request.json['template_issue_number']
    template_volume_number = request.json['template_volume_number']
    template_date = request.json['template_date']
    template_hoa = request.json['template_hoa']
    user_token = current_user_token.token

    template = Template(name, template_issue_number, template_volume_number, template_date, template_hoa, user_token=user_token)

    db.session.add(template)
    db.session.commit()

    response = template_schema.dump(template)
    return jsonify(response)

#show info in database
@api.route('/templates', methods = ['GET'])
@token_required
def get_template(current_user_token):
    a_user = current_user_token.token
    hoaTemps = Template.query.filter_by(user_token = a_user).all()
    response = template_schema.dump(hoaTemps)
    return jsonify(response)

#update template
@api.route('/templates/<id>', methods = ['POST', 'PUT'])
@token_required
def update_template(current_user_token, id):
    template = Template.query.get(id)
    template.name = request.json['name']
    template.template_issue_number = request.json['template_issue_number']
    template.template_volume_number = request.json['template_volume_number']
    template.template_date = request.json['template_date']
    template.template_hoa = request.json['template_hoa']
    template.saved_template = request.json['saved_template']
    template.user_token = current_user_token.token

    db.session.commit()
    response = template_schema.dump(template)
    return jsonify(response)

#update user
@api.route('/user<id>', methods = ['POST', 'PUT'])
@token_required
def update_user(current_user_token, id):
    user = User.query.get(id)
    user.first_name = request.json['first_name']
    user.last_name = request.json['last_name']
    user.hoa = request.json['hoa']
    user.phone_number = request.json['phone_number']
    user.email = request.json['email']
    user.user_token = current_user_token.token

    db.session.commit()
    response = user_schema.dump(user)
    return jsonify(response)

#delete template
@api.route('/templates/<id>', methods = ['DELETE'])
@token_required
def delete_template(current_user_token, id):
    template = Template.query.get(id)
    db.session.delete(template)
    db.session.commit()
    response = template_schema.dump(template)
    return jsonify(response)

#delete user
@api.route('/user/<id>', methods = ['DELETE'])
@token_required
def delete_user(current_user_token, id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    response = user_schema.dump(user)
    return jsonify(response)

