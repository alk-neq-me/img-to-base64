from flask import (
    Blueprint, render_template, request
)
from ..img_b64 import start


blue_print = Blueprint('convert', __name__, url_prefix="/")


@blue_print.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            file = request.files["image"]
            data = start(file, file.name)
            return render_template("home.html", data64=data)
    return render_template("home.html", data64="")
