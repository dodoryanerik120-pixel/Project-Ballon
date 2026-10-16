from flask import Blueprint, render_template, jsonify
from utils.database import sql

home_bp = Blueprint("home", __name__)

@home_bp.route("/", methods=["GET"])
def home():
    #result = sql("""
    #SELECT * FROM enigme ORDER BY id
    #""")

    user = "Toto"
    return render_template(
        "home.html",
        user=user
    )