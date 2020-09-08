from api import app
from flask import make_response, jsonify, request, Blueprint
import jwt
import datetime
from api.token_decorator import token_requiered

mainBp = Blueprint("mainBp", __name__)  # set up Bluprint


@app.route("/unprotected")
def unprotected():
    """unprotected route"""
    return "anyone can see this!"


@app.route("/protected")
@token_requiered
def protected(data):
    """protected route - only logged in users cam acess the data"""

    msg = {"messagem": "Your token is valid!", "data": data}
    return jsonify(msg)


@app.route("/login")
def login():
    auth = request.authorization

    if auth and auth.password == "password":

        token = jwt.encode(
            {
                "user": auth.username,
                "role": "regular",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            },
            app.config["SECRET_KEY"],
        )

        return jsonify({"token": token.decode("UTF-8")})

    return make_response(
        "could verify", 401, {"WWW-Authenticate": 'Basic realm="Login Required"'}
    )
