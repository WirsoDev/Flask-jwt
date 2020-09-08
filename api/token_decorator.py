"""Decorator for protected routes"""

from api import app
from functools import wraps
from flask import request, jsonify
import jwt


def token_requiered(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get("token")  # get the token directly from query string

        """Check if are not given a token"""
        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        """get de data"""
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
        except:
            return jsonify({"message": "Token is invalid!"}), 401

        """return args and pass data to use in function"""
        return f(data, *args, **kwargs)

    return decorated
