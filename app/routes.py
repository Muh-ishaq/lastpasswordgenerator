from flask import Blueprint, render_template, request, jsonify
from .utils import generate_password

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/generate", methods=["POST"])
def generate():
    data = request.json
    length = int(data.get("length", 12))
    modes = data.get("mode", [])
    password = generate_password(length, modes)
    return jsonify({"password": password})
