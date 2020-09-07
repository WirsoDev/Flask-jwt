from functools import wraps
from flask import jsonify
import jwt


def tokan_requiered(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        tokan = request.args.get('tokan')

        if not tokan:
            return jsonify({'message': 'Tokan is missing!'}), 403

        try:
            data = jwt.decode(tokan, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Tokan is invalid!'}), 403

        return f(*args, **kwargs)
