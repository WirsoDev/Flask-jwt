from flask import make_response, jsonify, request, Blueprint
import jwt
import datetime
from api.tokan_decorator import tokan_requiered
from api import app

main_bp = Blueprint('main_bp', __name__)


@app.route('/unprotected')
def unprotected():
    return 'data is not important!'


@app.route('/protected')
@tokan_requiered
def protected():
    return 'This dara is Importante!'


@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':

        tokan = jwt.encode({'user': auth.username, 'role': 'macaco',
                            'exp': datetime.datetime.utcnow(
                            ) + datetime.timedelta(minutes=30)},
                           app.config['SECRET_KEY'])

        return jsonify({'tokan': tokan.decode('UTF-8')})

    return make_response('could verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
